def bar_triang(a, b, c):  # points A, B and C will never be aligned
    x = (a[0] + b[0] + c[0]) / 3
    y = (a[1] + b[1] + c[1]) / 3
    return [round(x, 4), round(y, 4)]
