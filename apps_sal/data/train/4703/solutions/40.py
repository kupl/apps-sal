def bar_triang(a, b, c):  # points A, B and C will never be aligned
    return [round((a[i] + b[i] + c[i]) / 3, 4) for i in (0, 1)]
