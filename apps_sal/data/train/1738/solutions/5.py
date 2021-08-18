import itertools


def in_sphere(point, center, radius):
    dist = sum([(p - r)**2 for p, r in zip(point, center)])
    dist = dist**0.5
    return dist < radius and abs(dist - radius) / radius > 1e-10


def area(triangle_vertices):
    l1 = sum((triangle_vertices[0][i] - triangle_vertices[1][i])**2 for i in range(3))**0.5
    l2 = sum((triangle_vertices[0][i] - triangle_vertices[2][i])**2 for i in range(3))**0.5
    l3 = sum((triangle_vertices[1][i] - triangle_vertices[2][i])**2 for i in range(3))**0.5
    p = (l1 + l2 + l3) / 2
    A = (p * (p - l1) * (p - l2) * (p - l3))**0.5
    return A


def biggest_triang_int(point_list, center, radius):
    interior_points = [p for p in point_list if in_sphere(p, center, radius)]
    Triangles = []
    for triplet in itertools.combinations(interior_points, 3):
        Triangles.append((list(triplet), area(triplet)))

    num_tri = len(Triangles)
    if num_tri < 1:
        return []
    max_a = max(Triangles, key=lambda x: x[1])[1]
    winners = [T[0] for T in Triangles if abs(T[1] - max_a) < 0.01]
    if len(winners) == 1:
        return [num_tri, max_a, winners[0]]
    else:
        return [num_tri, max_a, winners]
    return 4
