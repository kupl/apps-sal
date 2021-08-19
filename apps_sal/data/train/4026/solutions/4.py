def d(a, b, c, d):
    return abs(d - b) + abs(c - a)


def optimum_location(st, lc):
    return 'The best location is number {} with the coordinates x = {} and y = {}'.format(*min(([sum((d(*n, i['x'], i['y']) for n in st)), i['id'], i['x'], i['y']] for i in lc))[1:])
