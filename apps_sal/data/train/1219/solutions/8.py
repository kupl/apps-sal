# cook your dish here
def pw(x,n):
    if x==0:
        return 1
    r=1
    while n>0:
        if n%2:
            r=(r*x)%1000000007
        x=(x*x)%1000000007
        n//=2
    return r%1000000007
t=int(input())
while t>0:
    n,m=list(map(int,input().split()))
    n//=2
    n*=n+1
    print(pw(m,n))
    t-=1


