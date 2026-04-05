"""Tests for quiz score storage."""

import unittest
from unittest.mock import Mock, patch

from quiz_app import storage


class StorageTests(unittest.TestCase):
    def test_load_best_score_returns_zero_when_file_is_missing(self) -> None:
        fake_path = Mock()
        fake_path.read_text.side_effect = FileNotFoundError

        with patch.object(storage, "STATS_FILE", fake_path):
            self.assertEqual(storage.load_best_score(), 0)

    def test_save_best_score_keeps_highest_value(self) -> None:
        fake_path = Mock()
        stored_data = {"content": None}

        def fake_read_text(*args, **kwargs):
            if stored_data["content"] is None:
                raise FileNotFoundError
            return stored_data["content"]

        def fake_write_text(content, *args, **kwargs):
            stored_data["content"] = content
            return len(content)

        fake_path.read_text.side_effect = fake_read_text
        fake_path.write_text.side_effect = fake_write_text

        with patch.object(storage, "STATS_FILE", fake_path):
            self.assertEqual(storage.save_best_score(80), 80)
            self.assertEqual(storage.save_best_score(65), 80)
            self.assertEqual(storage.load_best_score(), 80)


if __name__ == "__main__":
    unittest.main()
