from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    Merges overlapping intervals
    :param intervals: list
        intervals for a potential merge
    :return: list
        merged intervals
    """
    # Sort based on the lower bound
    intervals = sorted(intervals)

    # Initialize interval list with first element and remove it from interval list
    merged_intervals = [intervals.pop(0)]

    for i in intervals:
        # Look for overlapping interval at the end of the current merged intervals
        # Compare upper bound of last element of merged intervals and lower bound of input intervals
        if merged_intervals[-1][1] >= i[0]:
            # Intervals are overlapping -> merge
            new_interval = [merged_intervals[-1][0], max(merged_intervals[-1][1], i[1])]
            merged_intervals[-1] = new_interval
        else:
            # Intervals are not overlapping -> add to interval list
            merged_intervals += [i]

    return merged_intervals


if __name__ == "__main__":
    input_intervals = [[25, 30], [2, 19], [14, 23], [4, 8]]
    merge(intervals=input_intervals)
