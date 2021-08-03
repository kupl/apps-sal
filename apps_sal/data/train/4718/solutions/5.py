def x(n):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        result[i][i] = result[i][-i - 1] = 1
    return result
