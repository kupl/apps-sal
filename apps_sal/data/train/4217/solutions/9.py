from datetime import date


def solve(a, b):
    r = []
    for y in range(a, b + 1):
        for m in 1, 3, 5, 7, 8, 10, 12:
            d = date(y, m, 1)
            if d.weekday() == 4:
                r.append(d.strftime('%b'))
    return r[0], r[-1], len(r)
