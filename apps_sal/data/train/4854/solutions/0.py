def circum_curvat(points):
    A, B, C = [complex(*p) for p in points]
    BC, CA, AB = B - C, C - A, A - B
    D = 2. * (A.real * BC + B.real * CA + C.real * AB).imag
    if not D: return D, D
    U = (abs(A)**2 * BC + abs(B)**2 * CA + abs(C)**2 * AB) / D
    radius = (abs(BC) * abs(CA) * abs(AB)) / abs(D)
    return -1j * U, radius

def count_circles(circles, point):
    return sum(abs(complex(*point) - center) < radius
               for center, radius in map(circum_curvat, circles))
