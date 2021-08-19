def sum_of_intervals(intervals):
    return len(set([n for (a, b) in intervals for n in list(range(a, b))]))
