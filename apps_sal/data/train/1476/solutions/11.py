# your code goes here
from collections import defaultdict


def fac(num, modulo):
    ans = 1
    for i in range(2, num + 1):
        ans = (ans * i) % modulo
    return ans


def fast_expo(num, p, modulo):
    num %= modulo
    exxp = 1
    while(p > 0):
        if p & 1:
            exxp = exxp * num % modulo
        num = num * num % modulo
        p >>= 1
    return exxp


modulo = 1000000007

t = int(input())

for i in range(t):
    s = input().strip()

    mp = defaultdict(int)
    for si in s:
        mp[si] += 1

    denom = 1
    for alpha in mp.keys():
        denom = denom * fac(mp[alpha], modulo)
    denom = fast_expo(denom, modulo - 2, modulo)

    nfac = fac(len(s), modulo)
    nfac = nfac * denom % modulo

    print(int(nfac))
