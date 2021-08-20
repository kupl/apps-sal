from math import sqrt, hypot


def count_circles(list_of_circles, point):
    count = int(any((point in c for c in list_of_circles)))
    for [[x1, y1], [x2, y2], [x3, y3]] in list_of_circles:
        A = x1 * (y2 - y3) - y1 * (x2 - x3) + x2 * y3 - x3 * y2
        B = (x1 * x1 + y1 * y1) * (y3 - y2) + (x2 * x2 + y2 * y2) * (y1 - y3) + (x3 * x3 + y3 * y3) * (y2 - y1)
        C = (x1 * x1 + y1 * y1) * (x2 - x3) + (x2 * x2 + y2 * y2) * (x3 - x1) + (x3 * x3 + y3 * y3) * (x1 - x2)
        D = (x1 * x1 + y1 * y1) * (x3 * y2 - x2 * y3) + (x2 * x2 + y2 * y2) * (x1 * y3 - x3 * y1) + (x3 * x3 + y3 * y3) * (x2 * y1 - x1 * y2)
        [A, B, C, D] = map(float, [A, B, C, D])
        (xc, yc) = (-B / (2 * A), -C / (2 * A))
        r = sqrt((B * B + C * C - 4 * A * D) / (4 * A * A))
        d = hypot(point[0] - xc, point[1] - yc)
        if d <= r:
            count += 1
    return count
