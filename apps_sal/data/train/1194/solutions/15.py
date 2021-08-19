# cook your dish here
import sys
import math
from collections import Counter


def inputt():
    return sys.stdin.readline().strip()


def printt(n):
    sys.stdout.write(str(n) + '\n')


def listt():
    return [int(i) for i in inputt().split()]


def gcd(a, b):
    return math.gcd(a, b)


def lcm(a, b):
    return (a * b) / gcd(a, b)


t = int(inputt())


def SieveOfEratosthenes(n):
    s = 0
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):

        if (prime[p] == True):

            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    for p in range(n + 1):
        if prime[p]:
            s += p
    l = list(str(s))
    print(l[-1])


for _ in range(t):
    n = int(inputt())
    s = inputt()
    dic = Counter(s)
    c = 0
    c += abs(dic['U'] - dic['D']) + abs(dic['L'] - dic['R'])
    printt(n - c)
