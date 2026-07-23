import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")


def load_report():
    with REPORT_PATH.open() as f:
        return json.load(f)


def test_success_criterion_1_report_exists():
    """
    Success Criterion 1:
    Create /app/report.json.
    """
    assert REPORT_PATH.exists(), "report.json was not created"


def test_success_criterion_2_total_requests():
    """
    Success Criterion 2:
    report.json contains the correct total_requests value.
    """
    report = load_report()
    assert report["total_requests"] == 6


def test_success_criterion_3_unique_ips():
    """
    Success Criterion 3:
    report.json contains the correct unique_ips value.
    """
    report = load_report()
    assert report["unique_ips"] == 3


def test_success_criterion_4_top_path():
    """
    Success Criterion 4:
    report.json contains the correct top_path value.
    """
    report = load_report()
    assert report["top_path"] == "/index.html"
