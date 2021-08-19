import math
import bisect
import itertools
import sys
mod = 10 ** 9 + 7
'fact=[1]*1001\nifact=[1]*1001\nfor i in range(1,1001):\n    fact[i]=((fact[i-1])*i)%mod\n    ifact[i]=((ifact[i-1])*pow(i,mod-2,mod))%mod\ndef ncr(n,r):\n    return (((fact[n]*ifact[n-r])%mod)*ifact[r])%mod\ndef npr(n,r):\n    return (((fact[n]*ifact[n-r])%mod))\n    '
'def mindiff(a):\n    b=a[:]\n    b.sort()\n    m=10000000000\n    for i in range(len(b)-1):\n        if b[i+1]-b[i]<m:\n            m=b[i+1]-b[i]\n    return m\n    '
'def lcm(a,b):\n    return a*b//math.gcd(a,b)\n\n    '
'def merge(a,b):\n    i=0;j=0\n    c=0\n    ans=[]\n    while i<len(a) and j<len(b):\n        if a[i]<b[j]:\n            ans.append(a[i])\n            i+=1\n        else:\n            ans.append(b[j])\n            c+=len(a)-i\n            j+=1\n    ans+=a[i:]\n    ans+=b[j:]\n    return ans,c\ndef mergesort(a):\n    if len(a)==1:\n        return a,0\n    mid=len(a)//2   \n    left,left_inversion=mergesort(a[:mid])\n    right,right_inversion=mergesort(a[mid:])\n    m,c=merge(left,right)\n    c+=(left_inversion+right_inversion)\n    return m,c\n    \n'
'\ndef is_prime(num):\n    if num == 2: return True\n    if num == 3: return True\n    if num%2 == 0: return False\n    if num%3 == 0: return False\n    t = 5\n    a = 2\n    while t <= int(math.sqrt(num)):\n        if num%t == 0: return False\n        t += a\n        a = 6 - a\n    return True\n '
a1 = [2, 6]
a2 = [3, 18]
a = []
for i in range(100000):
    a2.append((a2[-1] + a1[-1] + 1) * 3 % mod)
    a1.append((a1[-1] + 1) * 2 % mod)
for i in range(100000):
    a.append(a1[i] + a2[i] + 1)
t = int(input())
for i in range(t):
    n = int(input())
    print(a[n - 1])
