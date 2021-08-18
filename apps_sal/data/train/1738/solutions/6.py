import itertools as it


def biggest_triang_int(point_list, center, radius):

    def dtc(p1, p2): return sum([(i - j)**2 for i, j in zip(p1, p2)])**(1.0 / 2)
    valid_points = [point for point in point_list if dtc(center, point) < radius]
    if len(valid_points) == 0:
        return []

    point_combinations = list(it.combinations(valid_points, 3))
    areas = []
    for i in point_combinations:
        a, b, c = dtc(i[0], i[1]), dtc(i[1], i[2]), dtc(i[2], i[0])
        S = (a + b + c) / 2
        areas.append(round((S * (S - a) * (S - b) * (S - c))**0.5, 8))

    pot_triangles, max_area, max_triangle_points = len(areas), max(areas), []

    if areas.count(max(areas)) == 1:
        max_triangle_points = list(point_combinations[areas.index(max(areas))])
    else:
        for c in range(areas.count(max(areas))):
            max_triangle_points.append([i for i in point_combinations[areas.index(max(areas))]])
            del point_combinations[areas.index(max(areas))]
            del areas[areas.index(max(areas))]

    return [pot_triangles, max_area, max_triangle_points]
