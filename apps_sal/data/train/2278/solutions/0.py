n = int(input())
rows = [input().split() for _ in range(n)]
rows = [(int(x), int(y)) for (x, y) in rows]
points = {}
for (x, y) in rows:
    if x in points:
        points[x] = max(y, points[x])
    else:
        points[x] = y
points = sorted(points.items(), key=lambda point: point[0])


def above(p, p1, p2):
    """
    x1 < x2
    y1 = x1^2 + bx1 + c
    y2 = x2^2 + bx2 + c
    y >? x^2 + bx + c

    y2 - y1 = x2^2 - x1^2 + bx2 - bx1
    b = (y2 - y1 - x2^2 + x1^2) / (x2 - x1)
    b * (x2 - x1) = y2 - y1 - x2^2 + x1^2

    c = y1 - x1^2 - bx1
    c * (x2 - x1) = (y1 - x1^2) * (x2 - x1) - x1 * (y2 - y1 - x2^2 + x1^2)

    y * (x2 - x1) >? (x^2 + bx + c) * (x2 - x1)
    y * (x2 - x1) >?
        x^2 * (x2 - x1)
        + x * (y2 - y1 - x2^2 + x1^2)
        + (y1 - x1^2) * (x2 - x1) - x1 * (y2 - y1 - x2^2 + x1^2)
    """
    (x, y) = p
    (x1, y1) = p1
    (x2, y2) = p2
    x_2 = x ** 2
    x12 = x1 ** 2
    x22 = x2 ** 2
    x2_x1 = x2 - x1
    eq_b = y2 - y1 - x22 + x12
    term_y = y * x2_x1
    term_x2 = x_2 * x2_x1
    term_x = x * eq_b
    term_c = (y1 - x12) * x2_x1 - x1 * eq_b
    return term_y >= term_x2 + term_x + term_c


Us = []
for (i, p) in enumerate(points):
    while len(Us) >= 2:
        (p1, p2) = Us[-2:]
        if above(p, p1, p2):
            Us.pop()
        else:
            break
    Us.append(p)
out = len(Us) - 1
print(out)
