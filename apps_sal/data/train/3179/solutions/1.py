def min_and_max(l, d, x):
    for n in range(l, d + 1):
        if sum(map(int, str(n))) == x:
            break

    for m in range(d, l - 1, -1):
        if sum(map(int, str(m))) == x:
            break

    return [n, m]
