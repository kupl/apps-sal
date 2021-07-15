def multiples(m, n):
    count = 1
    result = []
    for _ in range(m):
        result.append(n*count)
        count +=1
    return result
