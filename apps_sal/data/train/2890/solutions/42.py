def multiples(m, n):
    result = []
    x = 1
    for i in range(m):
        result.append(n * x)
        x += 1
    return result
