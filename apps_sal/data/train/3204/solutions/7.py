def Guess_it(n, m):
    lis = []
    for x in range(n + 1):
        for d in range(n - x + 1):
            if (5 * x) + (4 * d) + 3 * (n - x - d) == m:
                lis.append([x, d, (n - x - d)])
            else:
                pass
    return lis
