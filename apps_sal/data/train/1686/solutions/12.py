r, c, d = map(int, input().split())
l = []
for _ in range(r):
    l.append(list(map(int, input().split())))

dp = [[[0, 0] for _ in range(c)] for _ in range(r)]

dp[0][0] = [1, 1]
for j in range(r):
    for i in range(c):
        if l[j][i] == 0:
            continue
        for ii in range(i - 1, max(-1, i - 1 - d), -1):
            if l[j][ii] == 0:
                break
            dp[j][i][0] += dp[j][ii][1]

        for jj in range(j - 1, max(-1, j - 1 - d), -1):
            if l[jj][i] == 0:
                break
            dp[j][i][1] += dp[jj][i][0]
print(sum(dp[-1][-1]) % 20011)
