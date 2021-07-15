def combos(n):
    return combos_between(1, n)
def combos_between(m, n):
    if n == 1:
        return [[1]]
    result = [[n]]
    for x in range(m, n // 2 + 1):
        for combo in combos_between(x, n - x):
            result.append([x] + combo)
    return result
