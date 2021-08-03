def segments(m, a):
    return [p for p in range(m + 1) if all(not x[0] <= p <= x[1] for x in a)]
