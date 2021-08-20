(m, n) = map(int, input().split())
l = []
for _ in range(m):
    l.append(list(map(int, input().split())))
q = []
(m, n) = (0, 0)
for _ in range(int(input())):
    (y1, x1, y2, x2) = map(int, input().split())
    q.append([y1, x1, y2, x2])
    n = max(n, x2)
    m = max(m, y2)
dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
dp[1][1] = l[0][0]
for i in range(1, n + 1):
    dp[1][i] = dp[1][i - 1] + l[0][i - 1]
for j in range(2, m + 1):
    t_sum = 0
    for i in range(1, n + 1):
        t_sum += l[j - 1][i - 1]
        dp[j][i] = t_sum + dp[j - 1][i]
for (y1, x1, y2, x2) in q:
    ans = dp[y2][x2] - dp[y2][x1 - 1] - dp[y1 - 1][x2] + dp[y1 - 1][x1 - 1]
    print(ans)
