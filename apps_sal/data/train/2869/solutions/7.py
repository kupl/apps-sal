def distinct(s):
    return [e for (i, e) in enumerate(s) if e not in s[:i]]
