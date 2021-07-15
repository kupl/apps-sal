def maxlen(s1, s2):
    sm, lg = sorted((s1, s2))
    return min(max(lg / 3, sm), lg / 2)
