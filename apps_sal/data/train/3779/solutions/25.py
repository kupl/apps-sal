def past(h, m, s):
    return sum(a * b for a, b in zip([h, m, s], [3600, 60, 1])) * 1000
