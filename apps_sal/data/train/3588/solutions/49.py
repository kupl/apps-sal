def quadratic(x1, x2):
    # 0=x^2-(x1+x2)*x+x1*x2
    y = -(x1 + x2)
    t = (1, y, x1 * x2)
    return t
