for _ in range(int(input())):
    n,k = map(int,input().split()) ; m =(10**9)+7
    if n==0:
        if k==1:
            print(0)
        else:
            print((k*(k-1))%m)
    else:
        if k==1:
            print((n*(n-1)+n)%m)
        elif k%2:
            x = n+((k-1)//2)
            print((x*(x+1)-n)%m)
        else:
            x = (n+(k//2))
            print((x*(x-1)+n)%m)
