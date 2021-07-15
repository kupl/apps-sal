T=int(input())
for i in range(T):
    N=int(input())
    A=[int(i) for i in input().split()]
    m=0
    for i in range(N):
        if A[i]==0:
            m=m+1000
    for i in range(N):
        if A[i]==0:
            k=len(A)-i
            break
        else:
            k=0
    n=m+k*100
    print(n)
        
        
    

