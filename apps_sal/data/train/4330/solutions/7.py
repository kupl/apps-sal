def shortest_arrang(n):
    return (lambda ngm: next(((lambda x: list(range(x, x - ng, -1)))(int((2 * n + ng ** 2 - ng) / (2 * ng))) for ng in range(2, ngm + 1) if not (2 * n + ng ** 2 - ng) / (2 * ng) % 1), [-1]))(int(((1 + 8 * n) ** 0.5 - 1) / 2))
