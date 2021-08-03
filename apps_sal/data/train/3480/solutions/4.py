def sequence_sum(b, e, s):
    if (b > e and s > 0) or (b < e and s < 0):
        return 0
    k = (e - b) // s
    return b * (k + 1) + s * (k * (k + 1)) // 2
