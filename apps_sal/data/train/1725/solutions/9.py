def circular_limited_sums(max_n, max_fn):
    FL = [[0] * (max_fn + 1) for i in range(max_fn + 1)]
    for i in range(max_fn + 1):
        for j in range(max_fn + 1):
            if i == j:
                FL[i][j] = 1
    for x in range(max_n - 1):
        nextFL = [[0] * (max_fn + 1) for i in range(max_fn + 1)]
        for i in range(max_fn + 1):
            for j in range(max_fn + 1):
                for k in range(max_fn + 1):
                    if j + k <= max_fn:
                        nextFL[i][k] += FL[i][j]
        FL = nextFL
    tot = 0
    for i in range(max_fn + 1):
        for j in range(max_fn + 1):
            if i + j <= max_fn:
                tot += FL[i][j]
    return tot % 12345787
