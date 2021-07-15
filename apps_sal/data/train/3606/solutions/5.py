def find_pattern(a):
    diff = [a[i + 1] - a[i] for i in range(len(a) - 1)]
    l = len(diff)
    for i in range(1, len(diff) + 1):
        t = diff[:i]
        if l % len(t) == 0:
            if t * (l // len(t)) == diff:
                return t
