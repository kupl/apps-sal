def quadratic(x1, x2):
    x = 1
    f = (x * x, x * -x2, -x1 * x, -x1 * -x2)
    return (f[0], f[1] + f[2], f[3])
