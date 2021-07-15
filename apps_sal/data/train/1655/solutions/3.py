from collections import defaultdict
from itertools import combinations


def count_col_triang(points_colors):
    point_count = len(points_colors)

    colors = set(color for points, color in points_colors)
    color_count = len(colors)

    color_points = defaultdict(lambda: False)

    for c in colors:
        color_points[c] = [points
                           for points, color in points_colors if color == c]

    # get all with 3 or more points, kasi 3 points min sa triangle
    color_points = defaultdict(lambda: False, ((color, points)
                                               for color, points in color_points.items() if len(points) >= 3))

    triangle_count = 0
    color_triangle_count = defaultdict(lambda: False)

    for color, points in color_points.items():
        comb_points = combinations(points, 3)
        color_triangle_count[color] = 0
        x, y = 0, 1

        # get the side lengths and compute area
        for vertices in comb_points:
            va, vb, vc = vertices
            # get sides using distance between 2 points formula
            a = (((vb[x] - va[x])**2) + (vb[y] - va[y])**2)**0.5
            b = (((vc[x] - vb[x])**2) + (vc[y] - vb[y])**2)**0.5
            c = (((va[x] - vc[x])**2) + (va[y] - vc[y])**2)**0.5
            s = (a + b + c) / 2  # semi-perimeter
            area = (s*(s-a)*(s-b)*(s-c))**0.5

            # any 3 points with an area is a triangle
            if area != 0:
                triangle_count += 1
                color_triangle_count[color] += 1

    max_count = max(color_triangle_count.values())

    # get all colors with highest triangle count, append sa dulo count for format
    colors_max_count = sorted([color for color, count in color_triangle_count.items()
                               if count == max_count])
    colors_max_count.append(max_count)

    if max_count <= 0:
        colors_max_count = []

    return [point_count, color_count, triangle_count, colors_max_count]
