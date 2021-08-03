def find_pattern(a):
    d = [a[i + 1] - a[i] for i in range(len(a) - 1)]
    l = len(d)
    return next(d[:i] for i in range(1, len(d) + 1) if l % len(d[:i]) == 0 and d[:i] * (l // len(d[:i])) == d)
