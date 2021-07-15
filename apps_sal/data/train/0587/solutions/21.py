n=int(input())
l=list(map(int,input().split()))
ans=[]
for i in l:
    x=i^2
    if x==0:
        ans.append(i^3)
    else:
        ans.append(x)
print(*ans)

