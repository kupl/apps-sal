r, c = list(map(int, input().split()))
A = []
dp = [[0 for i in range(c + 1)] for j in range(r + 1)]
for i in range(r):
    A.append([int(j) for j in list(input())])

q = int(input())

for i in range(q):
    x1, y1, x2, y2 = list(map(int, input().split()))
    x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
    dp[x1][y1] += 1
    dp[x2 + 1][y2 + 1] += 1
    dp[x1][y2 + 1] -= 1
    dp[x2 + 1][y1] -= 1

for i, v1 in enumerate(A):
    for j, v2 in enumerate(v1):
        if i == 0 and j == 0:
            pass
        elif i == 0:
            dp[i][j] += dp[i][j - 1]
        elif j == 0:
            dp[i][j] += dp[i - 1][j]
        else:
            dp[i][j] += dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

        if dp[i][j] % 2 != 0:
            A[i][j] = 1 - A[i][j]
for i in A:
    for j in i:
        print(j, end="")
    print()
