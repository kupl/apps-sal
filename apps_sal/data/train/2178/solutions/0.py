inp = input().split(' ')
val = []

totNums = int(inp[0])
totOpt = int(inp[1])
inp = input().split(' ')  # assert(len(inp) == totNums)
for it in inp:
    val.append(int(it))

dp = [[0.0 for _ in range(0, totNums)] for __ in range(0, totNums)]
for i in range(0, totNums):
    for j in range(0, totNums):
        if val[i] > val[j]:
            dp[i][j] = 1.0

while totOpt > 0:
    totOpt -= 1

    inp = input().split(' ')
    fr = int(inp[0]) - 1
    to = int(inp[1]) - 1

    for i in range(0, totNums):
        if i != fr and i != to:
            dp[i][fr] = dp[i][to] = (dp[i][fr] + dp[i][to]) / 2
            dp[fr][i] = dp[to][i] = (dp[fr][i] + dp[to][i]) / 2

    dp[fr][to] = dp[to][fr] = (dp[fr][to] + dp[to][fr]) / 2

ans = 0.0
for i in range(0, totNums):
    for j in range(i + 1, totNums):
        ans += dp[i][j]

print('%.10f' % ans)
