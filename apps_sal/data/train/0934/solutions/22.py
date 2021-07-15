# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    l=list(map(int,input().split()))
    m=list(map(int,input().split()))
    n=list(map(int,input().split()))
    s=0
    for j in range(x):
        for k in range(y):
            for f in range(z):
                if l[j]<=m[k] and m[k]>=n[f]:
                    s=s+((l[j]+m[k])*(m[k]+n[f]))
    print(s%1000000007)
