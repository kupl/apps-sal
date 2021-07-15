for i in range(int(input())):
    n,k=map(int,input().split())
    if(n!=0):
        d=(k-1)//2
        z=n**2+(k//2)*(2*n)+d*(d+1)
        z=z%(10**9+7)
        print(z)
    else:
        z=k*(k-1)
        z=z%(10**9+7)
        print(z)
