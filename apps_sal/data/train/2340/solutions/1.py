import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    index = {e: i for (i, e) in enumerate(p)}
    m = 2 * n
    data = []
    for i in range(2 * n, 0, -1):
        temp = index[i]
        if temp < m:
            data.append(m - temp)
            m = temp
    m = len(data)
    dp = [[False for i in range(2 * n + 1)] for j in range(m + 1)]
    dp[0][0] = True
    for i in range(1, m + 1):
        for j in range(2 * n + 1):
            dp[i][j] = dp[i - 1][j] | dp[i - 1][j - data[i - 1]] & (j >= data[i - 1])
    if dp[m][n]:
        print('YES')
    else:
        print('NO')
