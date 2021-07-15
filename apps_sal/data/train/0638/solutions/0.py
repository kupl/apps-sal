for _ in range(int(input())):
    n,m=map(int,input().split())
    print("Case "+str(_+1)+":")
    for i in range(m):
        s=input()
        ls=len(s)
        if ls>n:
            print("0")
        else:
            k=(n-ls+1)
            print((k*pow(26,n-ls,1000000007))%1000000007)

