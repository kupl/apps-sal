from math import gcd
MOD = 1000000007
MOD2 = 998244353


def ii():
    return int(input())


def si():
    return input()


def dgl():
    return list(map(int, input()))


def f():
    return map(int, input().split())


def il():
    return list(map(int, input().split()))


def ls():
    return list(input())


for _ in range(ii()):
    n = ii()
    l = il()
    c = 0
    g = 0
    for i in range(n):
        g = gcd(g, l[i])
        if g == 1:
            c += 1
            g = 0
    print(c)
