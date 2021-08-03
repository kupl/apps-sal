from bisect import bisect_left
A = input()

N = len(A)
dp = [0] * (N + 2)
dp[N] = 1
d = [[N] for i in range(26)]
a = ord('a')
INF = float('inf')
for i in range(N - 1, -1, -1):
    d[ord(A[i]) - a].append(i)
    tmp = INF
    for j in range(26):
        tmp = min(tmp, dp[d[j][-1] + 1])
    dp[i] = tmp + 1


for i in range(26):
    d[i] = d[i][::-1]

pos = 0
ans = ''
for i in range(dp[0] - 1, -1, -1):
    for j in range(26):
        k = bisect_left(d[j], pos)
        if dp[d[j][k] + 1] == i:
            ans += chr(j + a)
            pos = d[j][k] + 1
            break

print(ans)
