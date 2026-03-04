import unittest

from analyze import compute_stats


class ComputeStatsTest(unittest.TestCase):
    def test_compute_stats_normal_case(self):
        values = [1.0, 2.0, 3.0, 4.0]

        stats = compute_stats(values)

        self.assertEqual(stats["count"], 4.0)
        self.assertEqual(stats["mean"], 2.5)
        self.assertEqual(stats["median"], 2.5)
        self.assertEqual(stats["min"], 1.0)
        self.assertEqual(stats["max"], 4.0)

    def test_compute_stats_single_value(self):
        values = [42.0]

        stats = compute_stats(values)

        self.assertEqual(stats["count"], 1.0)
        self.assertEqual(stats["mean"], 42.0)
        self.assertEqual(stats["median"], 42.0)
        self.assertEqual(stats["min"], 42.0)
        self.assertEqual(stats["max"], 42.0)


if __name__ == "__main__":
    unittest.main()
