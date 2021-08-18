from sys import stdin


def matrix(L, row, col, c):
    d = {}
    dp = []
    for i in range(row + 1):
        temp = []
        for i in range(col + 1):
            temp.append([])
        dp.append(temp)

    for i in range(row + 1):
        dp[i][0] = 0
    for i in range(col + 1):
        dp[0][i] = 0
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            if L[i - 1][j - 1] == c:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
            else:
                dp[i][j] = 0
            d[dp[i][j]] = d.get(dp[i][j], 0) + 1
    return d


n, m, q = list(map(int, stdin.readline().split()))
L = []
for i in range(n):
    L.append(stdin.readline().strip())
male = matrix(L, n, m, 'M')
female = matrix(L, n, m, 'F')
for i in range(q):
    query = stdin.readline().split()
    if query[1] == 'F':
        if female.get(int(query[0]), 0) == 0:
            print('no')
        else:
            print('yes')
    else:
        if male.get(int(query[0]), 0) == 0:
            print('no')
        else:
            print('yes')
