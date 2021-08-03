def multiples(m, n):
    i = 0
    u = 1
    results = []
    while i < m:
        results.append(u * n)
        i += 1
        u += 1
    return results
