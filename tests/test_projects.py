import csv
import sqlite3
import tempfile
import unittest
from pathlib import Path

from api_integration.extract_report import allowlisted, read_mock_pages, get_rows, ReportError
from book_adoption.etl import split_crn, old_term_code, run


class TestProjects(unittest.TestCase):
    def test_mock_reads_both_pages(self):
        self.assertEqual(len(read_mock_pages()), 3)

    def test_private_fields_are_not_exported(self):
        for record in allowlisted(read_mock_pages()):
            self.assertEqual(set(record), {"RecordID", "Category", "Status"})

    def test_rejects_bad_api_payload(self):
        with self.assertRaises(ReportError):
            get_rows({"DataRows": "not a list"})

    def test_course_reference(self):
        self.assertEqual(split_crn("12298|202610"), ("12298", "202610"))

    def test_old_term_mapping(self):
        self.assertEqual(old_term_code("J24"), "202420")
        self.assertEqual(old_term_code("G24"), "202510")

    def test_database_load(self):
        with tempfile.TemporaryDirectory() as temp:
            destination = str(Path(temp) / "demo.sqlite")
            stats = run(db_path=destination)
            self.assertEqual(stats["loaded"], 2)
            with sqlite3.connect(destination) as conn:
                data = conn.execute("SELECT crn, term_code FROM book_adoption WHERE source='A'").fetchone()
            self.assertEqual(data, ("12298", "202610"))


if __name__ == "__main__":
    unittest.main()
