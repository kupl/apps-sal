def infected_zeroes(s):
    m = 0
    l = 0
    for i, n in enumerate(s):
        if n == 0:
            m = i if l == 0 else max(m, (i - l + 1) // 2)
            l = i + 1
    return max(m, len(s) - l)
