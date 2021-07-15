def past(h, m, s):
    res = s * 1000
    res += m * 60 * 1000
    res += h * 60 * 60 * 1000
    return res
