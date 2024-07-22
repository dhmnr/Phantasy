## API Endpoint : /run_video_inference
Example :
```
from gradio_client import Client, handle_file

client = Client("http://localhost:7860/")
result = client.predict(
		prompt_text="Hello!!",
		resolution="480p",
		aspect_ratio="9:16",
		length="2s",
		motion_strength=5,
		aesthetic_score=6.5,
		use_motion_strength=False,
		use_aesthetic_score=True,
		camera_motion="none",
		reference_image=handle_file('https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png'),
		refine_prompt=False,
		fps=24,
		num_loop=1,
		seed=1024,
		sampling_steps=30,
		cfg_scale=7,
		api_name="/run_video_inference"
)
print(result)
```

## Accepts 16 parameters:

**prompt_text** `str` Required

The input value that is provided in the "Prompt" Textbox component.

**resolution** `Literal['144p', '240p', '360p', '480p', '720p']` Default: "480p"

The input value that is provided in the "Resolution" Radio component.

**aspect_ratio** `Literal['9:16', '16:9', '3:4', '4:3', '1:1']` Default: "9:16"

The input value that is provided in the "Aspect Ratio (H:W)" Radio component.

**length** `Literal['2s', '4s', '8s', '16s']` Default: "2s"

The input value that is provided in the "Video Length" Radio component.

**motion_strength** `float` Default: 5

The input value that is provided in the "Motion Strength" Slider component.

**aesthetic_score** `float` Default: 6.5

The input value that is provided in the "Aesthetic" Slider component.

**use_motion_strength** `bool` Default: False

The input value that is provided in the "Enable" Checkbox component.

**use_aesthetic_score** `bool` Default: True

The input value that is provided in the "Enable" Checkbox component.

**camera_motion** `Literal['none', 'pan right', 'pan left', 'tilt up', 'tilt down', 'zoom in', 'zoom out', 'static']` Default: "none"

The input value that is provided in the "Camera Motion" Radio component.

**reference_image** `filepath` Required

The input value that is provided in the "Image (optional)" Image component.

**refine_prompt** `bool` Default: False

The input value that is provided in the "Refine prompt with GPT4o" Checkbox component.

**fps** `float` Default: 24

The input value that is provided in the "FPS" Slider component.

**num_loop** `float` Default: 1

The input value that is provided in the "Number of Loops" Slider component.

**seed** `float` Default: 1024

The input value that is provided in the "Seed" Slider component.

**sampling_steps** `float` Default: 30

The input value that is provided in the "Sampling steps" Slider component.

**cfg_scale** `float` Default: 7

The input value that is provided in the "CFG Scale" Slider component.

## Returns 1 element

`Dict(video: filepath, subtitles: filepath | None)`

The output value that appears in the "Output Video" Video component.
