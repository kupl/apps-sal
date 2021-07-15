n,a,b=map(int,input().split())
x=list(map(int,input().split()))

kirikawari=int(b//a)

ans=0
for i in range(n-1):
    sa=x[i+1]-x[i]
    if sa<=kirikawari:
        ans+=sa*a
    else:
        ans+=b

print(ans)    
