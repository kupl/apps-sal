def regressionLine(x, y):
    n, sx, sy = len(x), sum(x), sum(y)
    sxy = sum(i * j for i, j in zip(x, y))
    sx_2, s_x2 = sx ** 2, sum(i * i for i in x)
    a = (s_x2 * sy - sx * sxy) / (n * s_x2 - sx_2)
    b = (n * sxy - sx * sy) / (n * s_x2 - sx_2)
    return round(a, 4), round(b, 4)
