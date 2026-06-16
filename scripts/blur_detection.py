import cv2
import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def detect_blur(blur_threshold: float):

    input_dir = BASE_DIR / "extracted_frames"

    accepted_dir = BASE_DIR / "accepted"

    rejected_dir = BASE_DIR / "rejected_blur"

    accepted_dir.mkdir(exist_ok=True)

    rejected_dir.mkdir(exist_ok=True)

    accepted = 0
    rejected = 0

    for image_path in input_dir.glob("*.jpg"):

        image = cv2.imread(str(image_path))

        if image is None:
            continue

        score = cv2.Laplacian(
            image,
            cv2.CV_64F
        ).var()

        if score < blur_threshold:

            shutil.copy(
                image_path,
                rejected_dir / image_path.name
            )

            rejected += 1

        else:

            shutil.copy(
                image_path,
                accepted_dir / image_path.name
            )

            accepted += 1

    print(f"Accepted: {accepted}")

    print(f"Rejected: {rejected}")

    return accepted, rejected