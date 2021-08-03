def sum_to_infinity(seq):
    r = seq[1] / seq[0]
    if not -1 < r < 1:
        return "No Solutions"
    res = seq[0] / (1 - r)
    return round(res, 3)
