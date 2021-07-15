for _ in range(int(input())):
    n,m=list(map(int,input().split()))
    n=n//2
    n=n*(n+1)
    n=int(n)
    print(pow(m,n,1000000007))

