def sum_of_intervals(intervals):
    sets = set()
    for a, b in intervals:
        sets.update(list(range(a, b)))
    return len(sets)
