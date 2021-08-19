def decomp(n):
    out = []
    for d in range(2, n + 1):
        if d == 2 or (d & 1 and d > 2 and all((d % i for i in range(3, 1 + int(d ** 0.5), 2)))):
            (a, x) = (0, n)
            while x >= d:
                x //= d
                a += x
            out.append((d, a))
    return ' * '.join([f'{i}^{j}' if j > 1 else str(i) for (i, j) in out])
