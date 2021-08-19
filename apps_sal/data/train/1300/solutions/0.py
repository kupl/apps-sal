from sys import stdin, stdout
from math import gcd
for _ in range(int(stdin.readline())):
    # n=int(stdin.readline()) k-pieces
    n, k = list(map(int, stdin.readline().split()))
    a = list(map(int, stdin.readline().split()))
    gr = [[0 for _ in range(n)]for _ in range(n)]
    ans = 0
    k -= 1
    for sz in range(n):
        for i in range(n - sz):
            j = i + sz
            if sz == 0:
                gr[i][j] = a[i]
            else:
                gr[i][j] = gcd(gr[i + 1][j], gr[i][j - 1])
    # print(*gr,sep='\n')
    dp = [[0 for _ in range(n)]for _ in range(k + 1)]
    for i in range(n):
        dp[0][i] = gr[0][i]
    for i in range(1, k + 1):
        for j in range(i, n):
            for par in range(j - 1, -1, -1):
                dp[i][j] = max(dp[i][j], gr[par + 1][j] + dp[i - 1][par])
    # print(*dp,sep='\n')
    print(dp[k][n - 1])
