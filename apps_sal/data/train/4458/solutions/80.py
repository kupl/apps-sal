def time_correct(t):
    if not t:
        return t
    if any([len(t) != 8, t[2] != ':', t[5] != ':', not all((x.isdigit() for x in t.split(':')))]):
        return None
    else:
        n = sum((int(x) * y for (x, y) in zip(t.split(':'), [3600, 60, 1])))
        return '{:02d}:{:02d}:{:02d}'.format(n // 3600 % 24, n // 60 - n // 3600 * 60, n % 60)
