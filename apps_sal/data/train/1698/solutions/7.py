from bisect import insort


def dbl_linear(n):
    u = [1]
    u0 = 123
    for i in range(n):
        while u[0] == u0:
            u.pop(0)
        u0 = u.pop(0)
        insort(u, 2 * u0 + 1)
        insort(u, 3 * u0 + 1)
    return u[0]
