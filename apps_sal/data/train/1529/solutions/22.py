def factorial(n):
    if n==1:
        return 1
    if n==0:
        return 1
    f=1
    for i in range(2,n+1):
        f=i*f
    return f
def cakes(A):
    num=sum(A)
    fact=factorial(len(A)-1)
    num=num*fact
    res=0
    n=len(A)
    i=1
    k=1
    while i<=n:
        res+=num*k
        k=10*k
        i+=1
    return res
t=int(input())
for i in range(t):
    n=int(input())
    A=[int(i) for i in input().split()][:n]
    print(cakes(A))
