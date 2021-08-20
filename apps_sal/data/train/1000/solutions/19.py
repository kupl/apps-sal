from collections import Counter
import string
import math
import sys
from fractions import Fraction


def array_int():
    return [int(i) for i in sys.stdin.readline().split()]


def vary(arrber_of_variables):
    if arrber_of_variables == 1:
        return int(sys.stdin.readline())
    if arrber_of_variables >= 2:
        return list(map(int, sys.stdin.readline().split()))


def makedict(var):
    return dict(Counter(var))


def printDivisors(n):
    divisors = []
    i = 1
    while i <= math.sqrt(n):
        if n % i == 0:
            if n // i == i:
                divisors.append(i)
            else:
                divisors.extend((i, n // i))
        i = i + 1
    return divisors


def countTotalBits(num):
    binary = bin(num)[2:]
    return len(binary)


def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True


' mod=10**9+7\ndef ncr(n,r):\n    if n<r:\n        return 0\n    numer=fact[n]\n    # print(numer)\n    denm=(fact[n-r]*fact[r])\n    # print(denm)\n    return numer*pow(denm,mod-2,mod) '
' def dfs(node):\n    nonlocal graph\n    mex=0\n    size=1\n    for i in graph[node]:\n        t=dfs(i)\n        mex=max(mex,t[0])\n        size+=t[1]\n    return [mex+size,size] '
' fact=[1]*(1001)\nc=1 \nmod=10**9+7\nfor i in range(1,1001):\n    fact[i]=(fact[i-1]*i)%mod '


def comp(x):
    return x[1]


for _ in range(vary(1)):
    n = vary(1)
    num = array_int()
    print(math.ceil(n / min(num)))
