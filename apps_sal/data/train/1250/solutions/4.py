import math
import bisect
import itertools
import sys
mod = 10**9 + 7
'''fact=[1]*1001
ifact=[1]*1001
for i in range(1,1001):
    fact[i]=((fact[i-1])*i)%mod
    ifact[i]=((ifact[i-1])*pow(i,mod-2,mod))%mod
def ncr(n,r):
    return (((fact[n]*ifact[n-r])%mod)*ifact[r])%mod
def npr(n,r):
    return (((fact[n]*ifact[n-r])%mod))
    '''
'''def mindiff(a):
    b=a[:]
    b.sort()
    m=10000000000
    for i in range(len(b)-1):
        if b[i+1]-b[i]<m:
            m=b[i+1]-b[i]
    return m
    '''
'''def lcm(a,b):
    return a*b//math.gcd(a,b)

    '''

'''def merge(a,b):
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
    
'''
'''
def is_prime(num):
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
 '''
a1 = [2, 6]
a2 = [3, 18]
a = []
for i in range(100000):
    a2.append(((a2[-1] + a1[-1] + 1) * 3) % mod)
    a1.append(((a1[-1] + 1) * 2) % mod)
for i in range(100000):
    a.append((a1[i] + a2[i] + 1) % mod)
t = int(input())
for i in range(t):
    n = int(input())
    print(a[n - 1])
