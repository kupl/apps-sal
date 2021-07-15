n=int(input())
a=list(map(int,input().split()))
b=[0,0]
ans=0
for i in range(n):
    b[a[i]]+=1
    if a[i]==0: ans+=b[1]
print(ans)

