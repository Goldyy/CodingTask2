import unittest

from main import merge


class TestMerge(unittest.TestCase):

    def test_merge(self):
        intervals = [[25, 30], [2, 19], [14, 23], [4, 8]]
        expected = [[2, 23], [25, 30]]
        merged_intervals = merge(intervals=intervals)
        self.assertEqual(merged_intervals, expected)

    # check if adjacent intervals are merged
    def test_merge_adjacent(self):
        intervals = [[25, 30], [21, 25], [11, 19], [31, 32]]
        expected = [[11, 19], [21, 30], [31, 32]]
        merged_intervals = merge(intervals=intervals)
        self.assertEqual(merged_intervals, expected)

    def test_no_merge(self):
        intervals = [[1, 3], [4, 10], [14, 23]]
        expected = [[1, 3], [4, 10], [14, 23]]
        merged_intervals = merge(intervals=intervals)
        self.assertEqual(merged_intervals, expected)


if __name__ == '__main__':
    unittest.main()
