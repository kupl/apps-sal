import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, M = mapint()
As = list(mapint())
mod = 10**9 + 7

SUM = sum(As)
ans = 1
for i in range(M-SUM+1, M+N+1):
    ans *= i
    ans %= mod

inv = 1
for i in range(1, SUM+N+1):
    inv *= i
    inv %= mod

print(ans*pow(inv, mod-2, mod)%mod)
