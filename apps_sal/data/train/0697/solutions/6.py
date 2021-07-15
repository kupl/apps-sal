# cook your dish here

def check(A,N,K):
    first = sum(A[:K])
    mx = sum(A[:K])
    for i in range(K,N):
        cur = first - A[i-K] + A[i]
        if(cur>mx):
            mx = cur
            first = cur
        else:
            first = cur
    return(mx)
        
    


t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    print(check(arr,n,k))
