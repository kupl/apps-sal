# dt = {} for i in x: dt[i] = dt.get(i,0)+1
def ipnl(n): return [int(input()) for _ in range(n)]


def inp(): return int(input())
def ip(): return [int(w) for w in input().split()]


M = 10**9 + 7
for _ in range(inp()):
    n, k = ip()
    if n == 0:
        t = k * (k - 1)
        print(t % M)
        continue
    if k == 1:
        print(n * n)
        continue
    kk = k // 2
    t = (n + kk) * (n + kk)
    if k % 2:
        t += kk
    else:
        t -= kk
    print(t % M)
