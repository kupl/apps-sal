'''
    Auther: ghoshashis545 Ashis Ghosh
    College: jalpaiguri Govt Enggineerin College
    Date:28/04/2020

'''
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right
from itertools import permutations
from datetime import datetime
from math import ceil, sqrt, log, gcd
def ii(): return int(input())
def si(): return input()
def mi(): return map(int, input().split())
def li(): return list(mi())


abc = 'abcdefghijklmnopqrstuvwxyz'
abd = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
mod = 1000000007
inf = float("inf")
vow = ['a', 'e', 'i', 'o', 'u']
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]


def powmod(a, b):
    a %= mod
    if(a == 0):
        return 0
    res = 1
    while(b > 0):
        if(b & 1):
            res = (res * a) % mod
        a = (a * a) % mod
        b >>= 1
    return res


def main():

    x = [0] * (1000005)
    n = ii()
    c = 0
    for i in range(n):
        x1, y1 = mi()
        x[x1 + 500001] += 1
        x[y1 + 500002] -= 1
        c = max(c, y1 + 500002)
    x[c] = 0
    s = 0
    for i in range(c):
        x[i] = (x[i] + x[i - 1]) % mod
        s = (s + x[i]) % mod
    print(s % mod)


def __starting_point():
    main()


__starting_point()
