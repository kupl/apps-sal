S = input()
N = len(S)
inf = 10 ** 18
nxt = [[N + 1] * 26 for _ in range(N + 2)]
for i in reversed(range(N)):
    for j in range(26):
        nxt[i][j] = nxt[i + 1][j]
    nxt[i][ord(S[i]) - ord('a')] = i
dp = [inf] * (N + 1)
dp[N] = 1
memo = [N] * (N + 1)
for i in reversed(range(N)):
    for (c, j) in enumerate(nxt[i]):
        if j > N:
            if dp[i] > 1:
                dp[i] = 1
                memo[i] = c
        elif dp[i] > dp[j + 1] + 1:
            dp[i] = dp[j + 1] + 1
            memo[i] = c
res = []
i = 0
while i <= N:
    res.append(chr(memo[i] + ord('a')))
    i = nxt[i][memo[i]] + 1
print(''.join(res))
