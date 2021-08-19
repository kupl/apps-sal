def past(h, m, s):
    return sum((u * c for (u, c) in zip((s, m, h), (1000, 60 * 1000, 60 * 60 * 1000))))
