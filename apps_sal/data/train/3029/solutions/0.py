def levenshtein(a,b):
    d = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

    d[0][:] = list(range(len(b)+1))
    for i in range(1, len(a) + 1):
        d[i][0] = i

    for i, x in enumerate(a):
        for j, y in enumerate(b):
            d[i+1][j+1] = min(1 + d[i][j+1], 1 + d[i+1][j], d[i][j] + (1 if x != y else 0))

    return d[-1][-1]


