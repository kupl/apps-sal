from math import hypot, sqrt


def how_to_find_them(t):
    if 'c' in t:
        (x, y) = 'ab' if 'b' in t else 'ba'
        return dict(t, **{x: sqrt(t['c'] ** 2 - t[y] ** 2)})
    return dict(t, c=hypot(t['a'], t['b']))
