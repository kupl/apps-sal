# cook your dish here
from sys import stdin,stdout
from math import gcd,sqrt,ceil
from copy import deepcopy
ii1=lambda:int(stdin.readline().strip())
is1=lambda:stdin.readline().strip()
iia=lambda:list(map(int,stdin.readline().strip().split()))
isa=lambda:stdin.readline().strip().split()
mod=1000000007
def power(base,power,modulus):
    res = 1
    while power:
        if power&1:
            res=(res*base)%modulus
        base=(base*base)%modulus
        power//=2
    return res
ma=1152921504606846976
t=ii1()
for i in range(t):
    n,k,x=map(int,input().split())
    for i in range(1,n+1):
        if i%k==0:
            print(x,end=' ')
        else:
            print(0,end=' ')
    print()

