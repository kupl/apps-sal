R,C=list(map(int,input().split()))
A=[]
for i in range(R):
    p=list(map(int,input().split()))
    A.append(p)
m, n = len(A), len(A[0])
for i in range(m):
    if A[i][0] == 0: 
        for j in range(n): A[i][j] ^= 1 
        
for j in range(n): 
    cnt=0
    for i in range(m):
        if(A[i][j]==1):
            cnt+=1
    if cnt < m - cnt: 
        for i in range(m): A[i][j] ^= 1

print(sum(int("".join(map(str, A[i])), 2) for i in range(m)))

