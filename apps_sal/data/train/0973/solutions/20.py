for i in range(int(input())):
    n,k=list(map(int,input().split()))
    l=list(map(int,input().split()))
    ma=max(l)+k
    mi=min(l)-k
    print(abs(ma-mi))

