def min_value(digits):
    s = list(set(digits))
    s.sort()
    t = 0
    for i in s:
        t = 10 * t + i
    return t
