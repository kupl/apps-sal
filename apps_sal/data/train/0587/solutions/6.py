n=int(input())
l=list(map(int,input().split()))
ans=[]
for i in l:
    if i==2:
        ans.append(1)
    else:
        ans.append(i^2)
print(*ans)
