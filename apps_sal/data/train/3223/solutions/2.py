def find_closest_value(m):
    x = int((m / 130)**0.5)
    y, z = 130 * x**2, 65 * x
    res = [y + v + i * z for i, v in enumerate((0, 4, 13, 69, 130))]
    return min(res, key=lambda k: (abs(m - k), m - k)) or 4
