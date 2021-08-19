from bisect import bisect
N = int(input())
xs = list(map(int, input().split()))
L = int(input())
Q = int(input())
qs = [tuple(map(lambda x: int(x) - 1, input().split())) for i in range(Q)]
K = len(bin(N)) - 1
dp = [[None] * N for i in range(K)]
for (i, x) in enumerate(xs):
    dp[0][i] = bisect(xs, x + L) - 1
for k in range(K - 1):
    for i in range(N):
        dp[k + 1][i] = dp[k][dp[k][i]]


def enough(fr, to, n):
    now = fr
    bn = bin(n)
    ln = len(bn) - 2
    for (i, c) in enumerate(bn[2:]):
        if c == '0':
            continue
        now = dp[ln - 1 - i][now]
        if now >= to:
            return True
    return False


ans = []
for (a, b) in qs:
    if a > b:
        (a, b) = (b, a)
    ok = N
    ng = 0
    while ok - ng > 1:
        m = (ok + ng) // 2
        if enough(a, b, m):
            ok = m
        else:
            ng = m
    ans.append(ok)
print(*ans, sep='\n')
