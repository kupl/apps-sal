def dbl_linear(n):
    u = [1]
    indexY = 0
    indexZ = 0

    def y(x):
        return 2 * x + 1

    def z(x):
        return 3 * x + 1
    while len(u) <= n:
        if y(u[indexY]) < z(u[indexZ]):
            if y(u[indexY]) != u[len(u) - 1]:
                u.append(y(u[indexY]))
            indexY += 1
        else:
            if z(u[indexZ]) != u[len(u) - 1]:
                u.append(z(u[indexZ]))
            indexZ += 1
    return u[n]
