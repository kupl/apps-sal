def Guess_it(n, m):
    result = []
    for x in range(0, n + 1):
        (b, r, g) = (4 * n + x - m, m - 3 * n - 2 * x, x)
        if all((y >= 0 for y in (b, r, g))):
            result.append([g, r, b])
    return result
