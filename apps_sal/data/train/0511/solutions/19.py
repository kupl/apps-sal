N=int(input())
A=list(map(int,input().split()))
allxor=A[0]
for j in range(1,N):
    allxor^=A[j]
ans=[]
for i in range(N):
    ans.append(allxor^A[i])
print(*ans,sep=" ")
