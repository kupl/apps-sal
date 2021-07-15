def multiples(m, n):
    count = 1
    result = []
    while count <= m:
        result.append(count * n)
        count += 1
    return result
