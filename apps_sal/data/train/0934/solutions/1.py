t=int(input())
for i in range(0,t):
    p,q,r=map(int,input().split())
    x=[int(x) for x in input().split()]
    y=[int(x) for x in input().split()]
    z=[int(x) for x in input().split()]
    s=0
    for j in range(0,p):
        for k in range(0,q):
            for l in range(0,r):
                if x[j]>y[k] or y[k]<z[l]:
                    s+=0
                else:
                    s+=(x[j]+y[k])*(y[k]+z[l])
    print(s%(10**9+7))
