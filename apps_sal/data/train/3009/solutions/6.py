def pairs(ar):
    return sum((1 for n in range(0, len(ar) - 1, 2) if abs(ar[n] - ar[n + 1]) == 1))
