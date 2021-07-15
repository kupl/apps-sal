n = int(input())
s = [0] * n
dp = [[0] for i in range(n)]
for i in range(n):
    dp[i] = list(map(int, input().split()))
for i in range(n):
    for j in range(n):
        s[i] = max(s[i], dp[i][j])
        s[j] = max(s[j], dp[i][j])
used = [False] * n
for i in range(n):
    if used[s[i] - 1]:
        s[i] *= -1
    else:
        used[s[i] - 1] = True
for i in range(n):
    if s[i] < 0:
        for j in range(1, n + 1):
            if abs(s[i]) < j and not used[j - 1]:
                s[i] = j
                break
print(*s)
