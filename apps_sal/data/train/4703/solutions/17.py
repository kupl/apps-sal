def bar_triang(a, b, c):  # points A, B and C will never be aligned
    # your code here
    x0 = (a[0] + b[0] + c[0]) / 3
    y0 = (a[1] + b[1] + c[1]) / 3
    return [round(x0, 4), round(y0, 4)]
