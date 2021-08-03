import sys
readline = sys.stdin.readline

N = int(readline())
A = list(map(int, readline().split()))

dp = [(a, 0) for a in A]
for i in range(N):
    for j in range(1 << N):
        if not j & (1 << i):
            k = j | (1 << i)
            a, b = dp[k]
            c, d = dp[j]
            res = None
            if a > c:
                if b > c:
                    res = (a, b)
                else:
                    res = (a, c)
            else:
                if a > d:
                    res = (c, a)
                else:
                    res = (c, d)
            assert res == tuple(sorted([a, b, c, d], reverse=True)[:2]), ''
            dp[k] = res
dp[0] = sum(dp[0])
for i in range(1, 1 << N):
    dp[i] = max(dp[i - 1], sum(dp[i]))
print('\n'.join(map(str, dp[1:])))
