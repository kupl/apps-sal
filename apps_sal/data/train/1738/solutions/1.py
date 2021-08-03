from itertools import combinations


def isclose(a, b): return abs(a - b) <= 10e-6
def distance(a, b, c, d, e, f): return ((d - a) ** 2 + (e - b) ** 2 + (f - c) ** 2) ** .5


def biggest_triang_int(points, center, r):
    valid = [i for i in points if distance(*(i + center)) <= r]
    filter_ = []
    for (a, b, c) in combinations(valid, 3):
        ab = distance(*(a + b))
        bc = distance(*(b + c))
        ac = distance(*(a + c))
        if ab + bc > ac and ab + ac > bc and bc + ac > ab:
            s = (ab + bc + ac) / 2
            area = (s * (s - ab) * (s - bc) * (s - ac)) ** .5
            filter_.append([[a, b, c], area])

    m = max(filter_, key=lambda x: x[1])[1] if filter_ else None
    ans = sorted([i[0] for i in filter_ if isclose(i[1], m)])

    return [len(filter_), m, ans[0] if len(ans) == 1 else ans] if m else []
