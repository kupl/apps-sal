def multiples(a, b):
    result = list()
    n = 1
    while a > 0:
        result.append(b * n)
        a -= 1
        n += 1
    return result
