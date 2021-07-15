# cook your dish here
p = (int)(1e9+7) 
for _ in range(int(input())):
    n,m =map(int,input().split())
    if n%2!=0:
        n=(n-1)//2
    else:
        n=n//2
    b=n*(n+1)
    ans=pow(m,b,p)
    print(ans)
