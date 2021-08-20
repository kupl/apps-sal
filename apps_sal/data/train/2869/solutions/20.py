def distinct(s):
    return [v for (i, v) in enumerate(s) if v not in s[:i]]
