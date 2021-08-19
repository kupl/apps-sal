def combs_non_empty_boxes(n, k):
    if n < k:
        return 'It cannot be possible!'
    if n == 0:
        return 0 if k == 0 else 1
    S = [[0] * (n + 1) for i in range(n + 1)]
    S[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            S[i][j] = S[i - 1][j - 1] + S[i - 1][j] * j
    return S[n][k]
