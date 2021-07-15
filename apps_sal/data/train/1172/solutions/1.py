from math import factorial
def Ncr(n,r):
    if r<0:return 0
    return factorial(n)/(factorial(n-r)*factorial(r))
def solve(m,n):
    modulo=10**9+7
    if m==n:
        return (Ncr(2*n-1,n-1)+Ncr(2*n-2,n-2))%modulo
    elif m>n:
        return (Ncr(m+n,n)-Ncr(m+n-2,n-1))%modulo
    else:
        return (Ncr(m+n,m)-Ncr(m+n-2,m-1))%modulo
        
t=int(input())
for i in range(t):
    inp=list(map(int,input()))
    m=inp.count(4)
    n=inp.count(7)
    print(solve(m,n))

