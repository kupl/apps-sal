def sum_of_intervals(intervals):
    result = set()
    for (start, end) in intervals:
        result |= set(range(start, end))
    return len(result)
