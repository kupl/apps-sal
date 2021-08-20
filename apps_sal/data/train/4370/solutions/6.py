def indices(n, d):
    result = ([i] for i in range(d + 1))
    for iteration in range(n - 1):
        result = (i + [j] for i in result for j in range(d + 1) if sum(i) + j <= d)
    return list(filter(lambda r: sum(r) == d, result))
