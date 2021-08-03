def dbl_linear(n):
    u = [1]
    i = 0
    j = 0
    while len(u) <= n:
        x = 2 * u[i] + 1
        y = 3 * u[j] + 1
        if x <= y:
            i += 1
        if x >= y:
            j += 1
        u.append(min(x, y))
    return u[n]
