import unittest
from memory_profiler import profile

from main import merge
import datetime


class TestMerge(unittest.TestCase):

    def setUp(self) -> None:
        self.start = datetime.datetime.now()

    def tearDown(self) -> None:
        self.end = datetime.datetime.now()
        self.duration = self.end - self.start
        print("{} took {} microseconds".format(self.__dict__['_testMethodName'], str(self.duration.microseconds)))

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

    def test_no_merge_large(self):
        intervals = [[x, x+2] for x in range(0, 10000000, 4)]
        expected = intervals
        merged_intervals = merge(intervals=intervals)
        self.assertEqual(merged_intervals, expected)

    @profile
    def test_profile_memory_consumption_small(self):
        self.test_no_merge()

    @profile
    def test_profile_memory_consumption_large(self):
        self.test_no_merge_large()


if __name__ == '__main__':
    unittest.main()
