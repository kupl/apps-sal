def multiples(m, n):
    result = []
    i = 1
    while i <= m:
        mul = n * i
        result.append(mul)
        i += 1
    return result
