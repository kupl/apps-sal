def sum_of_intervals(intervals):
    return len({a for interval in intervals for a in range(*interval)})
