def sum_of_intervals(intervals):

    merged = sorted([list(t) for t in intervals])
    i = 0
    while i < len(merged) - 1:
        if merged[i + 1][1] <= merged[i][1]:
            del merged[i + 1]
            continue
        if merged[i + 1][0] <= merged[i][1]:
            merged[i][1] = merged[i + 1][1]
            del merged[i + 1]
            continue
        i += 1

    return sum(b - a for a, b in merged)
