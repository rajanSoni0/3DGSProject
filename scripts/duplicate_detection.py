import shutil
from pathlib import Path

from PIL import Image
import imagehash

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_DIR = BASE_DIR / "accepted"

OUTPUT_DIR = BASE_DIR / "final_dataset"

DUPLICATE_DIR = BASE_DIR / "rejected_duplicate"

OUTPUT_DIR.mkdir(exist_ok=True)
DUPLICATE_DIR.mkdir(exist_ok=True)

HASH_THRESHOLD = 5

accepted_hashes = []

unique_count = 0
duplicate_count = 0

for image_path in INPUT_DIR.glob("*.jpg"):

    img = Image.open(image_path)

    current_hash = imagehash.average_hash(img)

    is_duplicate = False

    for existing_hash in accepted_hashes:

        if current_hash - existing_hash < HASH_THRESHOLD:
            is_duplicate = True
            break

    if is_duplicate:

        shutil.copy(
            image_path,
            DUPLICATE_DIR / image_path.name
        )

        duplicate_count += 1

    else:

        accepted_hashes.append(current_hash)

        shutil.copy(
            image_path,
            OUTPUT_DIR / image_path.name
        )

        unique_count += 1

print("\n===== DUPLICATE DETECTION REPORT =====")
print(f"Unique Images : {unique_count}")
print(f"Duplicates Removed : {duplicate_count}")