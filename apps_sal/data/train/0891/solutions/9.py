n,m=map(int,input().split())
ma=n*2+1
for i in range(m):
    x=int(input())
    if(x>n+1):
        z=abs(ma-x)
        print(n-z)
    else:
        print(0)

