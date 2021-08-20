def S2N(m, n):
    result = 0
    for i in range(0, m + 1):
        for j in range(0, n + 1):
            result += i ** j
    return result
