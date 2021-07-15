import math
def factorial(n,j):
    inf=998244353
    j[0]=1
    j[1]=1
    for i in range(2,n+1):
        j[i]=j[i-1]*i
        j[i]%=inf
    return j


l1=[0]*(200009)
y=factorial(200008,l1)
inf=998244353
n=int(input())
l=[0]*(200009)
x=1
for i in range(n-1):
    u,v=input().split()
    u,v=[int(u),int(v)]
    l[u]+=1
    l[v]+=1
for i in range(len(l)):
    if l[i]>0:
        x*=y[l[i]]
        x%=inf
print((n*x)%inf)

