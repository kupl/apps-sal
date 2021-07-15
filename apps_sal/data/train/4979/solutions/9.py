def count_deaf_rats(a):
    d = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i or j]
    d = {x:d[i] for i, x in enumerate("↖↑↗←→↙↓↘")}
    p, r = divmod("".join(a).index("P"), len(a[0])), 0
    for i, x in enumerate(a):
        for j, y in enumerate(x):
            if y not in " P":
                z = d[y]
                n = abs(i - p[0] + (j - p[1]) * 1j)
                m = abs(i + z[0] - p[0] + (j + z[1] - p[1]) * 1j)
                if n < m: r += 1
    return r
