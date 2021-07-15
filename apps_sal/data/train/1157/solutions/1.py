# cook your dish here
for i in range(int(input())):
    n,m,k=map(int,input().split())
    l,ans = list(map(int,input().split())),0
    for i in l:
        r=i//m + 1;c=i%m
        if(c==0):c=m;r-=1
        ans+=r*(n+1-r)*c*(m+1-c)
    ans/=((n+1)*(m+1)*n*m)//4
    print(ans)
