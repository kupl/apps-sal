def calc(k, n, m, x):

    f1 = 1
    f2 = 0
    fz2 = 0
    s = 0
    t = 0
    for i in range(1, n - 3):
        s += f2
        a = f1
        f1 = a + f2
        f2 = a
        if i == x - 3:
            t = s
            fz2 = f2

    A = (m - k * (s + 2)) / (s + f2)
    return A * (t + fz2) + k * (t + 2)
