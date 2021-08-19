def quadratic(x1, x2):
    a = 1  # given
    b = (a * - x2) + (a * - x1)  # (x-x1) * (x-x2) = 0
    c = -x1 * -x2
    return(a, b, c)


print(quadratic(1, 2))
