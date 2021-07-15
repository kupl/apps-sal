def closest(lst):
    m = min(abs(x) for x in lst)
    res = set(v for v in lst if abs(v) == m)
    return list(res)[0] if len(res) == 1 else None

