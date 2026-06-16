from pathlib import Path

from extract_frames import extract_frames
from blur_detection import detect_blur
from duplicate_detection import remove_duplicates
from report_generator import generate_report


def main():

    print("\n===== 3DGS PREPROCESSING PIPELINE =====\n")

    # User Inputs
    video_path = input(
        "Video Path [input_video/room.mp4]: "
    ).strip()

    if not video_path:
        video_path = "input_video/room.mp4"

    fps = int(
        input(
            "FPS for Frame Extraction [1]: "
        ) or 1
    )

    blur_threshold = float(
        input(
            "Blur Threshold [100]: "
        ) or 100
    )

    hash_threshold = int(
        input(
            "Duplicate Hash Threshold [5]: "
        ) or 5
    )

    # Validate Video Path
    project_root = Path(__file__).resolve().parent.parent

    full_video_path = project_root / video_path

    if not full_video_path.exists():

        print(
            f"\nVideo not found:\n{full_video_path}"
        )

        return

    # STEP 1
    print("\n===== STEP 1 : FRAME EXTRACTION =====")

    frames_extracted = extract_frames(
        video_path=video_path,
        fps=fps
    )

    # STEP 2
    print("\n===== STEP 2 : BLUR DETECTION =====")

    accepted_images, blurred_removed = detect_blur(
        blur_threshold=blur_threshold
    )

    # STEP 3
    print("\n===== STEP 3 : DUPLICATE DETECTION =====")

    final_images, duplicates_removed = remove_duplicates(
        hash_threshold=hash_threshold
    )

    # REPORT
    report = {

        "video_name":
            Path(video_path).name,

        "fps":
            fps,

        "frames_extracted":
            frames_extracted,

        "blurred_removed":
            blurred_removed,

        "duplicates_removed":
            duplicates_removed,

        "final_images":
            final_images
    }

    generate_report(report)

    # FINAL SUMMARY

    print("\n===== PIPELINE SUMMARY =====")

    print(
        f"Frames Extracted     : {frames_extracted}"
    )

    print(
        f"Blurred Removed      : {blurred_removed}"
    )

    print(
        f"Duplicates Removed   : {duplicates_removed}"
    )

    print(
        f"Final Dataset Images : {final_images}"
    )

    print("\nPipeline Completed Successfully")


if __name__ == "__main__":
    main()