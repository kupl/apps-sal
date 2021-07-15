from math import atan
def f(a,b,x,y):
    m=(a-x)/y
    n=(b-x)/y
    return atan(m)-atan(n)
for i in range(int(input())):
    c=int(input())
    b=list(map(int,input().split()))
    b.sort()
    x,y=map(int,input().split())
    s=0
    k=c//2
    for i in range(k):
        s += f(b[i],b[c-1-i],x,y)
    if s < 0:
        s = -s
    print(s)
