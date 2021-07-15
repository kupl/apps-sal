for i in range(int(input())):
    n,k=map(int,input().split())
    if k==0:
        print(n)
    else:
        if n%2==0:
            s=n//2 + (n//2)*(k+1)
            print(s)
        else:
            s=n//2 + 2*(k+1) + (n//2)*(k+1)
            print(s-1)
