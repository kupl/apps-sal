# author : Tapan Goyal
#           MNIT Jaipur

import math
import bisect
import itertools
import sys
I=lambda : sys.stdin.readline()
one=lambda : int(I())
more=lambda : map(int,I().split())
linput=lambda : list(more())

mod=10**9 +7
inf=10**18 + 1 

'''fact=[1]*100001
ifact=[1]*100001
for i in range(1,100001):
    fact[i]=((fact[i-1])*i)%mod
    ifact[i]=((ifact[i-1])*pow(i,mod-2,mod))%mod
def ncr(n,r):
    return (((fact[n]*ifact[n-r])%mod)*ifact[r])%mod
def npr(n,r):
    return (((fact[n]*ifact[n-r])%mod))
    '''


def merge(a,b):
    i=0;j=0
    c=0
    ans=[]
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            ans.append(a[i])
            i+=1
        else:
            ans.append(b[j])
            c+=len(a)-i
            j+=1
    ans+=a[i:]
    ans+=b[j:]
    return ans,c
def mergesort(a):
    if len(a)==1:
        return a,0
    mid=len(a)//2   
    left,left_inversion=mergesort(a[:mid])
    right,right_inversion=mergesort(a[mid:])
    m,c=merge(left,right)
    c+=(left_inversion+right_inversion)
    return m,c
    
def is_prime(num):
    if num == 1: return False
    if num == 2: return True
    if num == 3: return True
    if num%2 == 0: return False
    if num%3 == 0: return False
    t = 5
    a = 2
    while t <= int(math.sqrt(num)):
        if num%t == 0: return False
        t += a
        a = 6 - a
    return True

  
def ceil(a,b):
    return (a+b-1)//b
    


#/////////////////////////////////////////////////////////////////////////////////////////////////
def __starting_point():
    for _ in range(1):
        n=one()
        a=linput()
        for i in a:
            ans=i^2
            if ans>0:
                print(ans,end=" ")
            else:
                print(i^3,end=" ")
                
            
__starting_point()
