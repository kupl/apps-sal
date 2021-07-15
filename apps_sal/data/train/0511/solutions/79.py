N=int(input())
A=[int(x) for x in input().split()]
allxor=A[0]
for j in range(1,N):
    allxor^=A[j]
ans=[0]*N
for i in range(N):
    ans[i]=allxor^A[i]
print(*ans,sep=" ")
