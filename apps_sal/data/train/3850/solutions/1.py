def close_to_zero(t):
    n = min([int(s) for s in t.split()] or [0], key = abs)
    return abs(n) if str(-n) in t.split() else n
