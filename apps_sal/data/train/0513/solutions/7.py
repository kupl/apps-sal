import bisect
I = [int(_) for _ in open(0).read().split()]
N = I[0]
A = [0] + I[1:1 + N]
U = [0] + I[1 + N::2]
V = [1] + I[2 + N::2]
G = [set() for _ in range(N + 1)]
for u, v in zip(U, V):
    G[u].add(v)
    G[v].add(u)
ans = [10**10] * (N + 1)
stack = [(0, 1, 1, A[1], 0)]
dp = [-10 ** 10] + [10 ** 10] * N
while stack:
    i, j, p, q, d = stack.pop()
    if d:
        dp[p] = q
        continue
    stack += [(j, i, p, dp[p], 1)]
    dp[p] = q
    ans[j] = bisect.bisect_left(dp, 10 ** 10) - 1
    while G[j]:
        k = G[j].pop()
        if i == k:
            continue
        q = A[k]
        p = bisect.bisect_left(dp, q)
        stack += [(j, k, p, q, 0)]
print(*ans[1:], sep='\n')

