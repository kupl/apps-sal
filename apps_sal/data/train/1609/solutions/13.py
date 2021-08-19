def sum_of_intervals(intervals):
    return len(set([i for t in intervals for i in range(t[0], t[-1])]))
