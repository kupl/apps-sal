def S2N(m, n):
    result = 0
    for x in range(n + 1):
        for y in range(m + 1):
            result += y**x
    return result
