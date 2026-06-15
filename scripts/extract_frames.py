import subprocess
from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Paths
VIDEO_PATH = BASE_DIR / "input_video" / "room.mp4"
OUTPUT_DIR = BASE_DIR / "extracted_frames"

# Create output folder if it doesn't exist
OUTPUT_DIR.mkdir(exist_ok=True)

# Check if video exists
if not VIDEO_PATH.exists():
    print(f"Video not found: {VIDEO_PATH}")
    exit()

# FFmpeg command
command = [
    "ffmpeg",
    "-i",
    str(VIDEO_PATH),
    "-vf",
    "fps=5",
    str(OUTPUT_DIR / "frame_%04d.jpg")
]

print("Extracting frames...")

result = subprocess.run(
    command,
    capture_output=True,
    text=True
)

if result.returncode == 0:
    total_frames = len(list(OUTPUT_DIR.glob("*.jpg")))
    print(f"Frames extracted successfully!")
    print(f"Total Frames: {total_frames}")
else:
    print("Extraction Failed")
    print(result.stderr)