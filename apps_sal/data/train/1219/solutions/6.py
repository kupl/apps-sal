for _ in range(int(input())):
    mod=(10**9)+7
    n,m=map(int,input().split())
    n=n-(n%2)
    num=n//2
    ##print(num)
    tot=(num*((2*num)+2))//2

    print(pow(m,tot,mod))
