t=int(input())
for _ in range(t):
    n=int(input())
    p=10**9+7
    a=(pow(3,n+1,p)-1)
    b=(pow(2,n+1,p)-1)
    print((((3*a)//2)%p-(2*(b))%p)%p)
