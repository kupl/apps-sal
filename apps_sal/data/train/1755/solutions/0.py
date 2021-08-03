def splitlist(l):
    half = sum(l) // 2
    sums = [(0, [])]
    for i, n in enumerate(l):
        sums = sums + [(m + n, a + [i]) for m, a in sums if m + n <= half]
        if max(s[0] for s in sums) == half:
            break
    sums.sort(key=lambda v: abs(v[0] - half))
    indices = sums[0][1]
    return [n for i, n in enumerate(l) if i in indices], [n for i, n in enumerate(l) if i not in indices]
