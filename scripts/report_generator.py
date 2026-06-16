import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def generate_report(report_data):

    reports_dir = BASE_DIR / "reports"

    reports_dir.mkdir(exist_ok=True)

    report_file = reports_dir / "preprocessing_report.json"

    with open(report_file, "w") as f:
        json.dump(
            report_data,
            f,
            indent=4
        )

    print(
        f"Report Generated: {report_file}"
    )