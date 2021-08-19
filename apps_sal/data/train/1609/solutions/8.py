def sum_of_intervals(intervals):
    return len(set([i for (a, b) in intervals for i in range(a, b)]))
