def more_zeros(s):
    return list(dict.fromkeys((x for (x, y) in zip(s, map(bin, map(ord, s))) if y.count('0') << 1 > len(y))))
