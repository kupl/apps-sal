for _ in range(int(input())):
    n,k=map(int,input().split())
    if k==0:
        print(n)
    elif n%2==0:
        print((k+1)*n//2+n//2)
    else:
        print((k+1)*(n//2)+n//2+2*k+1)
