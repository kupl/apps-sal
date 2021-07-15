t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))[:n]
    m=max(arr)
    mi=min(arr)
    a=(m-mi)+2*k
    print(a)
