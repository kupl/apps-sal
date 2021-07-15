from sys import stdin, stdout
from math import ceil, floor, gcd, fabs, factorial, fmod, sqrt, inf
from bisect import bisect_left as bl, bisect_right as br, bisect
mod = pow(10, 9) + 7
mod2 = 998244353
def inp(): return stdin.readline().strip()
def out(var, end="\n"): stdout.write(str(var)+"\n")
def outa(*var, end="\n"): stdout.write(' '.join(map(str, var)) + end)
def lmp(): return list(mp())
def mp(): return list(map(int, inp().split()))
def smp(): return list(map(str, inp().split()))
def l1d(n, val=0): return [val for i in range(n)]
def l2d(n, m, val=0): return [l1d(n, val) for j in range(m)]
def remadd(x, y): return 1 if x%y else 0

def chkprime(x):
    if x<=1: return False
    if x in (2, 3): return True
    if x%2 == 0: return False
    for i in range(3, int(sqrt(x))+1, 2):
        if x%i == 0: return False
    return True

l = []
i = 2
while True:
    if i**4 > 10**18: break
    if chkprime(i):
        l.append(i**4)
    i += 1

for _ in range(int(inp())):
    n = int(inp())
    k = br(l, n)
    print(k)
    

