from itertools import combinations


def grad(a, b):
    """Builds a gradient description"""
    rise, tread = b[1] - a[1], b[0] - a[0]
    if rise == 0 or tread == 0:
        if rise == tread:
            return "p"  # Single point
        elif rise == 0:
            return "y"  # Y Axis constant
            # return "y={}".format(a[0])
        return "x"  # X Axis constant
    else:
        # Warning: Float used in comparison later, could be a problem
        # but not likely given integer inputs
        return rise / tread


def collinear(a, b, c):
    """Determines if three points are colinear"""
    return grad(a, b) == grad(b, c)


def count_col_triang(input_):
    # Group the inputs based on colour, to unique points within each colour
    colors = set(map(lambda t: t[1], input_))
    points = {col: set() for col in colors}
    for coord, color in input_:
        points[color].add(tuple(coord))

    # Discard any colours with less than 3 unique points
    # Geometry fact: Need at least 3 points to form a triangle!
    points = {k: list(sorted(v)) for k, v in points.items() if len(v) > 2}

    total = 0
    counts = {}
    for color, point_list in points.items():
        count = 0
        # Generate all possible trios of potential triangle vertices
        for a, b, c in combinations(point_list, 3):
            # Make sure the points are not collinear
            if not collinear(a, b, c):
                # Yay! we found a triangle
                count += 1
        counts[color] = count
        total += count

    # Identify colours with greatest number of triangles
    most_count = max(counts.values())
    most = [c for c, n in counts.items() if n == most_count]
    most = [] if most_count == 0 else (list(sorted(most)) + [most_count])

    # Collate stats and return
    return [len(input_), len(colors), total, most]
