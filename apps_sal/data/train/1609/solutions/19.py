def sum_of_intervals(intervals):

    # Merge the intervals so that all intervals are disjoint
    merged = sorted([list(t) for t in intervals])
    i = 0
    while i < len(merged) - 1:
        if merged[i + 1][1] <= merged[i][1]:
            # Next interval is a subset of current interval
            del merged[i + 1]
            continue
        if merged[i + 1][0] <= merged[i][1]:
            # Next interval has some overlap with currenrt interval
            merged[i][1] = merged[i + 1][1]
            del merged[i + 1]
            continue
        i += 1

    # Calculate the sum of the disjoint intervals
    return sum(b - a for a, b in merged)
