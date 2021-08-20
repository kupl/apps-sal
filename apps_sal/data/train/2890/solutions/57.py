def multiples(m, n):
    luvut = list(range(1, m + 1))
    _ = map(lambda luku: luku * n, luvut)
    return list(_)
