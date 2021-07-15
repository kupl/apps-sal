from itertools import combinations

def distance(*pair):
    return sum((u - v) ** 2 for u, v in zip(*pair)) ** .5

def area(*vertices):
    sides = [distance(*p) for p in combinations(vertices, 2)]
    return (sum(d**2for d in sides)**2 - 2 * sum(d**4for d in sides)) ** .5 / 4

def biggest_triang_int(point_list, center, radius):
    points = [p for p in point_list if distance(center, p) < radius]
    triangles = [[area(*t), list(t)] for t in combinations(points, 3)]
    if not triangles: return []
    max_area = max(triangles)[0]
    best_triangles = [t for a, t in triangles if a == max_area]
    return [len(triangles), max_area, best_triangles if len(best_triangles) > 1 else best_triangles.pop()]
