# cook your dish here
import bisect
MAXR = 100
MAXN = 20000000
T = int(input().strip())
queries = []
for t in range(T):
    L, R = map(int, input().strip().split())
    queries.append((L, R))
    MAXR = max(MAXR, R + 1)
MOD = 10**9 + 7
g = [0, 1, 2]
p = [0, 1, 3]
s = [0, 1, 9]
for n in range(3, MAXN):
    gg = 1 + g[n - g[g[n - 1]]]
    pp = p[n - 1] + gg
    ss = (s[n - 1] + gg * n * n) % MOD
    g.append(gg)
    p.append(pp)
    s.append(ss)
    if pp > MAXR:
        break


def process(m):
    n = bisect.bisect_right(p, m)
    return (s[n - 1] + (m - p[n - 1]) * n * n) % MOD


for L, R in queries:
    print((process(R) - process(L - 1)) % MOD)
