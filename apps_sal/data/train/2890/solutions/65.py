def multiples(m, n):
    result = []
    count = 1
    for a in range(m):
        result.append(count*n)
        count += 1

    return result
