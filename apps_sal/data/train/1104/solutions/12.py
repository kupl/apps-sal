# import sys
# sys.stdin = open('input.txt','r')
# sys.stdout = open('output1.txt','w')
import math
from sys import stdin,stdout
from math import gcd,sqrt,ceil,floor,inf
from copy import deepcopy
ii1=lambda:int(stdin.readline().strip())
is1=lambda:stdin.readline().strip()
iia=lambda:list(map(int,stdin.readline().strip().split()))
isa=lambda:stdin.readline().strip().split()
mod=1000000007
# fib=[1,1]
# a=1
# b=1
# for i in range(100001):
#     a,b=b,a+b
#     fib.append(b%mod)
# print(fib[0:10])
for _ in range(ii1()):
    n,k=iia()
    new=k-1
    if n==0:
        if k==1:
            ans=0
        else:
            ans=(k-1)*(k)
    elif k==1:
        ans=n*(n+1)-n
    elif k%2==0:
        ans=(n+(new//2))*(n+(new//2)+1)+n
    else:
        ans=(n+(new//2))*(n+(new//2)+1)-n
    print(ans%mod)







