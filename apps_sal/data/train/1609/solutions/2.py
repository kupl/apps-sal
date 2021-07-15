def sum_of_intervals(intervals):
    return len(set([n for (a, b) in intervals for n in [i for i in range(a, b)]]))
