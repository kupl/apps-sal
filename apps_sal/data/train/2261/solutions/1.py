from collections import deque
(n, m, v) = map(int, input().split())
(x, t, b, bt, dp, mi, mi2, mi3, dpmin, dp2) = ([0] * 300, [0] * 300, 0, 0, [[0] * 2 for i in range(150001)], 0, 100000000000000, 10000000000000, 0, [0] * 150001)
d = deque()
for i in range(m):
    (x[i], b, t[i]) = map(int, input().split())
    bt += b
for i2 in range(m - 1):
    if i2 == 0:
        for i in range(1, n + 1):
            dp[i][0] = abs(i - x[0])
            if mi2 > dp[i][0]:
                mi2 = dp[i][0]
    if m == 1:
        break
    if (t[i2 + 1] - t[i2]) * v >= n:
        mi3 = mi2
        mi2 = 1000000000000000000
        for i in range(1, n + 1):
            dp[i][0] = mi3 + abs(i - x[i2 + 1])
            if mi2 > dp[i][0]:
                mi2 = dp[i][0]
        continue
    mi2 = 1000000000000000000
    for i in range(1, n + 1 + (t[i2 + 1] - t[i2]) * v):
        if i <= n:
            while len(d) > 0 and dp[i][0] <= d[len(d) - 1][0]:
                d.pop()
            dp[i][1] = i + 2 * (t[i2 + 1] - t[i2]) * v + 1
            d.append(dp[i])
        if d[0][1] == i:
            d.popleft()
        if i - (t[i2 + 1] - t[i2]) * v >= 1:
            dp2[i - (t[i2 + 1] - t[i2]) * v] = d[0][0] + abs(x[i2 + 1] - (i - (t[i2 + 1] - t[i2]) * v))
    for i in range(1, n + 1):
        dp[i][0] = dp2[i]
        if dp2[i] < mi2:
            mi2 = dp2[i]
    d.clear()
for i in range(1, n + 1):
    if i == 1:
        mi = dp[i][0]
    if dp[i][0] < mi:
        mi = dp[i][0]
print(bt - mi)
