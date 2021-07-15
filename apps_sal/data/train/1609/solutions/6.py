def sum_of_intervals(intervals):
    return len(set().union(*[list(range(*item))for item in intervals]))
