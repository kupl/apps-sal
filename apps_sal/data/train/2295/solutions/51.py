N=int(input())
A=[0 for i in range(N)]
B=[0 for i in range(N)]
for i in range(N):
    A[i],B[i]=list(map(int,input().split()))
X=[]
for i in range(N):
    if A[i]>B[i]:
        X.append(B[i])
if len(X)==0:
    print((0))
else:
    print((sum(A)-min(X)))

