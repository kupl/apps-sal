import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def LS2(): return list(sys.stdin.readline().rstrip())


N,M = MI()
A = LI()
s = sum(A)
mod = 10**9+7

if s > M:
    print((0))
    return

# (M+N)_C_(s+N)

a = 1
for i in range(1,s+N+1):
    a *= i
    a %= mod

ans = pow(a,mod-2,mod)
for i in range(s+N):
    ans *= M+N-i
    ans %= mod

print(ans)

