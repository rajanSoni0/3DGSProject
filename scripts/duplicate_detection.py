import shutil
from pathlib import Path

from PIL import Image
import imagehash

BASE_DIR = Path(__file__).resolve().parent.parent


def remove_duplicates(hash_threshold: int):

    input_dir = BASE_DIR / "accepted"

    final_dir = BASE_DIR / "final_dataset"

    duplicate_dir = BASE_DIR / "rejected_duplicate"

    final_dir.mkdir(exist_ok=True)

    duplicate_dir.mkdir(exist_ok=True)

    hashes = []

    unique_count = 0
    duplicate_count = 0

    for image_path in input_dir.glob("*.jpg"):

        img = Image.open(image_path)

        current_hash = imagehash.average_hash(img)

        is_duplicate = False

        for existing_hash in hashes:

            if current_hash - existing_hash < hash_threshold:
                is_duplicate = True
                break

        if is_duplicate:

            shutil.copy(
                image_path,
                duplicate_dir / image_path.name
            )

            duplicate_count += 1

        else:

            hashes.append(current_hash)

            shutil.copy(
                image_path,
                final_dir / image_path.name
            )

            unique_count += 1

    print(f"Unique Images: {unique_count}")

    print(f"Duplicates Removed: {duplicate_count}")

    return unique_count, duplicate_count