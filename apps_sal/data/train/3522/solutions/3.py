def max_gap(n):
    n.sort()
    return max(a-b for a, b in zip(n[1:], n))
