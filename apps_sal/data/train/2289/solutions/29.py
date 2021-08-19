S = input()
N = len(S)
INF = N + 1
nex = [[INF] * 26 for _ in range(N + 1)]
for (i, c) in enumerate(S[::-1]):
    ic = ord(c) - ord('a')
    for j in range(26):
        nex[N - i - 1][j] = N - i - 1 if j == ic else nex[N - i][j]
dp = [N] * (N + 3)
dp[INF] = dp[INF + 1] = 0
for i in range(N, -1, -1):
    tmp = INF
    for j in range(26):
        tmp = min(tmp, dp[nex[i][j] + 1] + 1)
        if tmp == 1:
            break
    dp[i] = tmp
ans = []
i = 0
for v in range(dp[0] - 1, -1, -1):
    for j in range(26):
        if dp[nex[i][j] + 1] != v:
            continue
        ans.append(chr(j + ord('a')))
        i = nex[i][j] + 1
        break
print(''.join(ans))
