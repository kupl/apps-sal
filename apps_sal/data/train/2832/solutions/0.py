def array_equalization(a, k):
    totals, ends = {}, {}
    for i, n in enumerate(a):
        if n not in ends: totals[n], ends[n] = 0, -1
        if i < ends[n]: continue
        count = (i - ends[n] - 1 + k - 1) // k
        totals[n] += count
        ends[n] = max(i, ends[n] + count * k)
    return min(t + (len(a) - ends[n] - 1 + k - 1) // k
               for n, t in totals.items() if ends[n] < len(a))
