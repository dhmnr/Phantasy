from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
import asyncio
import uuid
import os
from typing import Dict

app = FastAPI()

class VideoRequest(BaseModel):
    prompt: str
    duration: int

class VideoResponse(BaseModel):
    id: str
    status: str

#TODO : Unrestricted File Download Vuln

VIDEO_DIR = "generated_videos"
os.makedirs(VIDEO_DIR, exist_ok=True)

video_tasks: Dict[str, asyncio.Task] = {}


async def generate_video(video_id: str, prompt: str, duration: int):
    try:
        # Simulate video generation process
        await alcm_generate(prompt, duration)  # Simulating the time it takes to generate a video
        
        # In a real implementation, you would generate the video here
        video_path = os.path.join(VIDEO_DIR, f"{video_id}.mp4")
        with open(video_path, "wb") as f:
            f.write(b"")  # Write empty content for demonstration
        
        return "completed"
    except Exception as e:
        return f"failed: {str(e)}"

@app.post("/generate-video", response_model=VideoResponse)
async def create_video(video_request: VideoRequest):
    video_id = str(uuid.uuid4())
    
    # Create a task for video generation
    task = asyncio.create_task(generate_video(video_id, video_request.prompt, video_request.duration))
    video_tasks[video_id] = task
    
    return VideoResponse(id=video_id, status="processing")

@app.get("/video-status/{video_id}", response_model=VideoResponse)
async def get_video_status(video_id: str):
    task = video_tasks.get(video_id)
    if not task:
        return VideoResponse(id=video_id, status="not_found")
    
    if task.done():
        status = await task
        # Clean up the task
        del video_tasks[video_id]
    else:
        status = "processing"
    
    return VideoResponse(id=video_id, status=status)

@app.get("/download-video/{video_id}")
async def download_video(video_id: str):
    video_path = os.path.join(VIDEO_DIR, f"{video_id}.mp4")
    if not os.path.exists(video_path):
        raise HTTPException(status_code=404, detail="Video not found")
    
    return FileResponse(video_path, media_type="video/mp4", filename=f"{video_id}.mp4")