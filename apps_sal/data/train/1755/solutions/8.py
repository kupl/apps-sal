
def splitlist(lst):

    if not lst:
        return ([], [])
    target = sum(lst) // 2

    dp = [[0 for _ in range(target + 1)] for _ in range(len(lst) + 1)]

    for i in range(1, len(lst) + 1):
        for j in range(target + 1):
            if j >= lst[i - 1]:

                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - lst[i - 1]] + lst[i - 1])

            else:
                dp[i][j] = dp[i - 1][j]

    seg1 = []

    w = target
    for i in range(len(lst), -1, -1):
        if dp[i][w] - dp[i - 1][w - lst[i - 1]] == lst[i - 1]:
            seg1.append(lst[i - 1])
            w -= lst[i - 1]

    seg2 = [a for a in lst]
    for a in seg1:
        seg2.remove(a)

    return (seg1, seg2)
