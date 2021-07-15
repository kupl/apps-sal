import sys
from random import choice,randint
inp=sys.stdin.readline
out=sys.stdout.write
flsh=sys.stdout.flush
 
sys.setrecursionlimit(10**9)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
 
def MI(): return map(int, inp().strip().split())
def LI(): return list(map(int, inp().strip().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines().strip()]
def LI_(): return [int(x)-1 for x in inp().strip().split()]
def LF(): return [float(x) for x in inp().strip().split()]
def LS(): return inp().strip().split()
def I(): return int(inp().strip())
def F(): return float(inp().strip())
def S(): return inp().strip()
def pf(s): return out(s+'\n')
def JA(a, sep): return sep.join(map(str, a))
def JAA(a, s, t): return s.join(t.join(map(str, b)) for b in a)

def main():
    t = I()
    l = []
    for _ in range(t):
        n,k=MI()
        a=LI()
        lcf=[0]*n
        lce=[0]*n
        for i in range(n):
            cnt1,cnt2=0,0
            for j in a[:i]:
                if j<a[i]:
                    cnt1+=1
            for j in a[i:]:
                if j<a[i]:
                    cnt2+=1
            lcf[i]=cnt1
            lce[i]=cnt2
        ans=0
        for i in range(n):
            ans += lcf[i]*((k*(k-1))//2)
        for i in range(n):
            ans += lce[i]*((k*(k+1))//2)
        l.append(ans)

    for i in range(t):
        pf(str(l[i]))

def __starting_point():
    main()
__starting_point()
