import json
import unittest
from pathlib import Path

from src.analyzer import build_report, run


class AnalyzerTests(unittest.TestCase):
    def test_build_report_counts_records(self) -> None:
        report = build_report([
            {"query_id": "q_11", "workload": "finance", "compute_seconds": 62, "cache_hit": False},
            {"query_id": "q_12", "workload": "finance", "compute_seconds": 8, "cache_hit": True},
        ])
        self.assertEqual(report["record_count"], 2)

    def test_run_writes_output(self) -> None:
        output_path = Path("out/test-report.json")
        report = run(Path("data/queries.ndjson"), output_path)
        on_disk = json.loads(output_path.read_text(encoding="utf-8"))
        self.assertEqual(report["record_count"], 4)
        self.assertIn("workloads", on_disk)


if __name__ == "__main__":
    unittest.main()
