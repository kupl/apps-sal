def find_a(a, n):
    if 0 <= n < len(a):
        return a[n]

    if n < 0:
        n = 3 - n
        a = a[::-1]

    b = [None] * 4
    b[1] = 3*a[1] - a[0] - a[2]
    b[2] = 3*a[2] - a[1] - a[3]
    b[0] = 3*b[1] - a[1] - b[2]
    b[3] = 3*b[2] - b[1] - a[2]
    for _ in range(n-3):
        x = 3*a[-1] - b[-1] - a[-2]
        y = 3*b[-1] - a[-1] - b[-2]
        a.append(x)
        b.append(y)
    return a[-1]
