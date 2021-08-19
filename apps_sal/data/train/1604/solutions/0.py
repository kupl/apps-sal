def getSum(dp, pos, s, e, type_):
    if e < s:
        return 0

    if type_ == 'D':
        if e == m - 1:
            return dp[pos][s]
        return dp[pos][s] - dp[pos][e + 1]
    else:
        if e == n - 1:
            return dp[s][pos]
        return dp[s][pos] - dp[e + 1][pos]


mod = 10**9 + 7
n, m = map(int, input().split())
a = [list(list(map(lambda x: 1 if x == 'R' else 0, input()))) for _ in range(n)]

SD = [[0] * m for _ in range(n)]
SN = [[0] * m for _ in range(n)]
dpD = [[0] * m for _ in range(n)]
dpN = [[0] * m for _ in range(n)]

for i in range(n - 1, -1, -1):
    for j in range(m - 1, -1, -1):
        if i == n - 1:
            SD[i][j] = a[i][j]
        else:
            SD[i][j] = SD[i + 1][j] + a[i][j]

        if j == m - 1:
            SN[i][j] = a[i][j]
        else:
            SN[i][j] = SN[i][j + 1] + a[i][j]

for j in range(m - 1, -1, -1):
    if a[n - 1][j] == 1:
        break
    dpD[n - 1][j] = 1
    dpN[n - 1][j] = 1

for i in range(n - 1, -1, -1):
    if a[i][m - 1] == 1:
        break
    dpD[i][m - 1] = 1
    dpN[i][m - 1] = 1

for j in range(m - 2, -1, -1):
    if i == n - 1:
        break
    dpD[n - 1][j] += dpD[n - 1][j + 1]

for i in range(n - 2, -1, -1):
    if j == m - 1:
        break
    dpN[i][m - 1] += dpN[i + 1][m - 1]

for i in range(n - 2, -1, -1):
    for j in range(m - 2, -1, -1):
        s, e = j, m - SN[i][j] - 1
        #print(i, j, s, e, 'N')
        dpN[i][j] = getSum(dpD, i + 1, s, e, 'D')
        dpN[i][j] = (dpN[i][j] + dpN[i + 1][j]) % mod

        s, e = i, n - SD[i][j] - 1
        #print(i, j, s, e, 'D')
        dpD[i][j] = getSum(dpN, j + 1, s, e, 'N')

    if i != 0:
        for j in range(m - 2, -1, -1):
            dpD[i][j] = (dpD[i][j] + dpD[i][j + 1]) % mod

print(dpD[0][0] % mod)
