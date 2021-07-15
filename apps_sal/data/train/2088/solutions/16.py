n = int(input())
c = [*map(int, input().split())]
inf = n + 1
dp = [[inf for _ in range(n)] for __ in range(n)]

def find(l, r):
    if l > r:
        return 0
    if l == r or (l == r - 1 and c[l] == c[r]):
        dp[l][r] = 1
        return 1
    if dp[l][r] != inf:
        return dp[l][r]
    m = 1 + find(l + 1, r)
    for i in range(l + 2, r + 1):
        if c[l] == c[i]:
            m = min(m, find(l + 1, i - 1) + find(i + 1, r))
    if c[l] == c[l + 1]:
        m = min(m, find(l + 2, r) + 1)
    dp[l][r] = m
    return m

mi = inf
for i in range(n):
    mi = min(find(0, i) + find(i + 1, n - 1), mi)
print(mi)
