n = int(input())
l = []
dp = []
d = {}
for i in range(n):
    l.append(int(input()))
    d[i] = []
    dp.append([0, 0])
for i in range(n - 1):
    (a, b) = list(map(int, input().split()))
    d[a - 1].append(b - 1)
    d[b - 1].append(a - 1)


def dfs(ch, pa, visited):
    dp[ch][1] = l[ch]
    for i in range(len(d[ch])):
        if d[ch][i] not in visited:
            visited.add(d[ch][i])
            dfs(d[ch][i], ch, visited)
            dp[ch][0] += max(dp[d[ch][i]][0], dp[d[ch][i]][1])
            dp[ch][1] += dp[d[ch][i]][0]


v = set()
v.add(0)
dfs(0, -1, v)
print(max(dp[0][0], dp[0][1]))
