import cv2
import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_DIR = BASE_DIR / "extracted_frames"
ACCEPTED_DIR = BASE_DIR / "accepted"
REJECTED_DIR = BASE_DIR / "rejected_blur"

ACCEPTED_DIR.mkdir(exist_ok=True)
REJECTED_DIR.mkdir(exist_ok=True)

BLUR_THRESHOLD = 100

accepted = 0
rejected = 0

for image_path in INPUT_DIR.glob("*.jpg"):

    image = cv2.imread(str(image_path))

    if image is None:
        continue

    score = cv2.Laplacian(
        image,
        cv2.CV_64F
    ).var()

    print(f"{image_path.name} -> {score:.2f}")

    if score < BLUR_THRESHOLD:

        shutil.copy(
            image_path,
            REJECTED_DIR / image_path.name
        )

        rejected += 1

    else:

        shutil.copy(
            image_path,
            ACCEPTED_DIR / image_path.name
        )

        accepted += 1

print("\n===== REPORT =====")
print(f"Accepted : {accepted}")
print(f"Rejected : {rejected}")