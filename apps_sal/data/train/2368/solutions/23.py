import sys
# sys.setrecursionlimit(10**6) 
input=sys.stdin.readline
t=int(input())
for t1 in range(t):
    n=int(input())
    a=list(map(int,input().split(" ")))
    b=list(map(int,input().split(" ")))
    a1=min(a)
    b1=min(b)
    ans=0
    for i in range(n):
        f1=0
        f2=0
        if(a[i]>a1):
            f1=a[i]-a1
        if(b[i]>b1):
            f2=b[i]-b1
        z=min(f1,f2)
        ans+=z
        f1-=z
        f2-=z
        ans+=f1+f2
    print(ans)
