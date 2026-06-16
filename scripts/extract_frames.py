import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def extract_frames(video_path: str, fps: int):

    video_file = BASE_DIR / video_path
    output_dir = BASE_DIR / "extracted_frames"

    output_dir.mkdir(exist_ok=True)

    command = [
        "ffmpeg",
        "-y",
        "-i",
        str(video_file),
        "-vf",
        f"fps={fps}",
        str(output_dir / "frame_%04d.jpg")
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise Exception(result.stderr)

    total_frames = len(list(output_dir.glob("*.jpg")))

    print(f"Frames Extracted: {total_frames}")

    return total_frames