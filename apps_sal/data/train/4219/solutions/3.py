def maxlen(*s):
    a, b = min(s), max(s)
    return b / 3 if b > a * 3 else b / 2 if b < a * 2 else a
