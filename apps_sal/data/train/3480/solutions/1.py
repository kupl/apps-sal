def sequence_sum(b, e, s):
    q, r = divmod(e - b, s)
    return (b + e - r) * max(q + 1, 0) // 2
