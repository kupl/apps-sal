def sum_of_intervals(intervals):
    result = set()
    for start, stop in intervals:
        for x in range(start, stop):
            result.add(x)
            
    return len(result)
