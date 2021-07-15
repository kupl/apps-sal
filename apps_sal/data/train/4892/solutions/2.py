from itertools import combinations

def find_biggTriang(points):
    num_triplets = num_triangles = 0
    max_area, max_triangles = 0, []
    for triangle in map(list, combinations(map(list, points), 3)):
        num_triplets += 1
        (ax, ay), (bx, by), (cx, cy) = triangle
        area = abs(ax * (by - cy) + bx * (cy - ay) + cx * (ay - by)) / 2
        if not area: continue
        num_triangles += 1
        if area > max_area: max_area, max_triangles = area, []
        if area == max_area: max_triangles.append(triangle)
    return [len(points), num_triplets, num_triangles,
            max_triangles.pop() if len(max_triangles) == 1 else max_triangles, max_area]
