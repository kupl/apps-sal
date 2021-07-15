import sys

readline = sys.stdin.readline
readall = sys.stdin.read
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prn = lambda x: print(*x, sep='\n')


def solve():
    n, k = nm()
    s = list(map(int, list(ns())))
    w = sum(s)
    sc = n
    for i in range(k):
        t = s[i::k]
        m = len(t)
        dp = [[0]*3 for j in range(m+1)]
        for j in range(m):
            dp[j+1][0] = dp[j][0] + t[j]
            dp[j+1][1] = min(dp[j][0], dp[j][1]) + 1 - t[j]
            dp[j+1][2] = min(dp[j][1], dp[j][2]) + t[j]
        sc = min(sc, min(dp[m]) + w - sum(t))
    print(sc)
    return




# solve()

T = ni()
for _ in range(T):
    solve()

