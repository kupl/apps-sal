T=int(input())
for t in range(T):
    N=int(input())
    X=list(map(int,input().split())) 
    mx=0
    for i in range(N):
        if mx<X[i%N]+X[(i+1)%N]+X[(i+2)%N]:
            mx=X[i%N]+X[(i+1)%N]+X[(i+2)%N]
    print(mx) 
