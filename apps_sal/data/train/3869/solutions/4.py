def tr(n):
    return n * (n + 1) // 2 if n >= 0 else 0


def shape_area(n):
    return tr(n) + 2 * tr(n - 1) + tr(n - 2)
