def N(): return int(input())
def NM():return map(int,input().split())
def L():return list(NM())
def LN(n):return [N() for i in range(n)]
def LL(n):return [L() for i in range(n)]
t=N()
from math import gcd
def f():
    n,m,a,b=NM()
    if n*a!=m*b:
        print("NO")
        return
    print("YES")
    ans=[[0]*m for i in range(n)]
    t=0
    for i in range(n):
        for j in range(a):
            ans[i][(j+t)%m]=1
        t+=a
    for i in ans:
        print("".join(map(str,i)))
for i in range(t):
    f()
