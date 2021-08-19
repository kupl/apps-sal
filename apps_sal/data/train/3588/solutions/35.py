def quadratic(x1, x2):
    a = 1
    b = a * -x2 + a * -x1
    c = -x1 * -x2
    return (a, b, c)


print(quadratic(1, 2))
