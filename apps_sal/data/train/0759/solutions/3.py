# cook your dish here
from collections import Counter


# Python3 program to find prime factorization
# of a number n in O(Log n) time with
# precomputation allowed.
import math as mt

MAXN = 100001

# stores smallest prime factor for
# every number
spf = [0 for i in range(MAXN)]

# Calculating SPF (Smallest Prime Factor)
# for every number till MAXN.
# Time Complexity : O(nloglogn)


def sieve():
    spf[1] = 1
    for i in range(2, MAXN):

        # marking smallest prime factor
        # for every number to be itself.
        spf[i] = i

    # separately marking spf for
    # every even number as 2
    for i in range(4, MAXN, 2):
        spf[i] = 2

    for i in range(3, mt.ceil(mt.sqrt(MAXN))):

        # checking if i is prime
        if (spf[i] == i):

            # marking SPF for all numbers
            # divisible by i
            for j in range(i * i, MAXN, i):

                # marking spf[j] if it is
                # not previously marked
                if (spf[j] == j):
                    spf[j] = i

# A O(log n) function returning prime
# factorization by dividing by smallest
# prime factor at every step


def getFactorization(x):
    ret = list()
    while (x != 1):
        ret.append(spf[x])
        x = x // spf[x]

    return ret.pop()  # last ele

# Driver code


# precalculating Smallest Prime Factor
sieve()
# x = 12246

# calling getFactorization function
# p = getFactorization(x)

# for i in range(len(p)):
#     print(p[i], end = " ")

# This code is contributed
# by Mohit kumar 29


t = int(input())

for test in range(t):
    n = int(input())
    A = tuple(map(int, input().split()))
    li = []
    mx = 1
    mx_li = []
    for a in A:
        li.append(getFactorization(a))

    c = Counter(li)
    # print(li)
    # print(c)
    for key in c:
        if c[key] > mx:
            mx_li = [key]
            mx = c[key]
        elif c[key] == mx:
            mx_li.append(key)

    print(max(mx_li))
