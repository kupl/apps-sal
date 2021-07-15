def modinv(v,m):
    v %= m
    pv = m
    pc = 0
    c = 1
    while v > 0:
     q, a = divmod(pv, v)
     pc, c = c, pc-q*c
     pv, v = v, a
    return pc % m

def binmod(n,r,m):
    if 2*r > n: r = n - r
    if r < 0: return 0
    if r == 0: return 1
    tp = 1
    bm = 1
    for t in range(1, r+1):
     bm = bm*t%m
     tp = tp*(n+1-t)%m
    return (tp*modinv(bm,m))%m

MVAL = 1000000007
for ti in range(int(input())):
    n,k,m = map(int,input().split())
    ays = list(map(int,input().split()))
