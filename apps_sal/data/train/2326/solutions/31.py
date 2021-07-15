N = int(input())
L = [0] + list(map(int,input().split()))
D = {}
D[0] = [0,0]
for i in range(1,N+1):
    if L[i] not in D:
        D[L[i]] = [i,1]
    else:
        D[L[i]][1] += 1

A = list(D.items())
A.sort(reverse=True)
#print(A)

ans=0
ANS = [0 for i in range(N+1)]

for i in range(1,len(D)):
    ANS[A[i-1][1][0]] += (A[i-1][0] - A[i][0]) * A[i-1][1][1]
    A[i][1][0] = min(A[i-1][1][0],A[i][1][0])
    A[i][1][1] += A[i-1][1][1]

for i in range(1,len(ANS)):
    print(ANS[i])
