def zata(N, A):
    dp = A[:]
    for n in range(N):
        bit = 1 << n
        for i in range(1 << N):
            if i & bit:
                dp[i] = merge(dp[i ^ bit], dp[i])
    return dp


def merge(x, y):
    return sorted(x + y)[:2]


N = int(input())
A, res = [], 0
for a in map(int, input().split()):
    A.append([-a])
for a, b in zata(N, A)[1:]:
    res = min(res, a + b)
    print(-res)
