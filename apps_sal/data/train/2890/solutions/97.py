def multiples(m, n):
    count = 1
    results = []
    while count <= m:
        results.append(count * n)
        count += 1
    return results
