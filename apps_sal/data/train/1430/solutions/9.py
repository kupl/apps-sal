for _ in range(int(input())):
    n,k=map(int,input().split())
    if(n%2==0):
        ans=n+(n//2)*k
        print(ans)
    else:
        n=n-1
        ans=n+(n//2)*k+1+2*k
        print(ans)
