from itertools import combinations


def grad(a, b):
    """Builds a gradient description"""
    rise, tread = b[1] - a[1], b[0] - a[0]
    if rise == 0 or tread == 0:
        if rise == tread:
            return "p"
        elif rise == 0:
            return "y"
        return "x"
    else:
        return rise / tread


def collinear(a, b, c):
    """Determines if three points are colinear"""
    return grad(a, b) == grad(b, c)


def count_col_triang(input_):
    colors = set(map(lambda t: t[1], input_))
    points = {col: set() for col in colors}
    for coord, color in input_:
        points[color].add(tuple(coord))

    points = {k: list(sorted(v)) for k, v in points.items() if len(v) > 2}

    total = 0
    counts = {}
    for color, point_list in points.items():
        count = 0
        for a, b, c in combinations(point_list, 3):
            if not collinear(a, b, c):
                count += 1
        counts[color] = count
        total += count

    most_count = max(counts.values())
    most = [c for c, n in counts.items() if n == most_count]
    most = [] if most_count == 0 else (list(sorted(most)) + [most_count])

    return [len(input_), len(colors), total, most]
