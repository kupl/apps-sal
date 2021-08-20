from itertools import groupby


def london_city_hacker(journey):
    arr = list(map(type, journey))
    s = 0
    for (k, g) in groupby(arr):
        g = len(list(g))
        if k == str:
            s += 2.4 * g
        else:
            s += 1.5 * (g // 2 + (1 if g % 2 else 0) if g > 1 else g)
    return f'£{round(s, 2):.2f}'
