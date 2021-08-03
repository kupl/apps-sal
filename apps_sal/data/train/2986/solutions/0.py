def segments(m, arr):
    return [i for i in range(m + 1) if not any(a <= i <= b for a, b in arr)]
