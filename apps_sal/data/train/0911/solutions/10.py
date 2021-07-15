import bisect
import sys
input = sys.stdin.readline

MAXR = 100
MAXN = 20000000

t = int(input().strip())
queries = []
for t in range(t):
 L, R = map(int, input().strip().split())
 queries.append((L,R))
 MAXR = max(MAXR, R + 1)
 
 
MOD = 10 ** 9 + 7
g = [0, 1, 2]
p = [0, 1, 3]
s = [0, 1, 9]

for n in range(3, MAXN):
 gn = 1 + g[n - g[g[n - 1]]]
 pn = p[n - 1] + gn
 sn = (s[n - 1] + gn * n * n) % MOD
 g.append(gn)
 p.append(pn)
 s.append(sn)
 if pn > MAXR:
  break
 
def process(m):
 n = bisect.bisect_right(p, m)
 return (s[n - 1] + (m -p[n - 1]) * n * n) % MOD
 
 
for L, R in queries:
 print(process(R) - process(L - 1) % MOD)
