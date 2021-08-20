"""input
3
a.ba
c...c
...
"""
from collections import defaultdict as dd
from collections import Counter as ccd
from itertools import permutations as pp
from itertools import combinations as cc
from random import randint as rd
from bisect import bisect_left as bl
from bisect import bisect_right as br
import heapq as hq
from math import gcd
"\nAuthor : dhanyaabhirami\nHardwork beats talent if talent doesn't work hard\n"
'\nStuck?\nSee github resources\nDerive Formula\nKmcode blog\nCP Algorithms Emaxx\n'
mod = pow(10, 9) + 7


def inp(flag=0):
    if flag == 0:
        return list(map(int, input().strip().split(' ')))
    else:
        return int(input())


t = inp(1)
while t:
    t -= 1
    s = input().strip()
    n = len(s)
    s = list(s)
    if n % 2 == 1 and s[n // 2] == '.':
        s[n // 2] = 'a'
    for i in range(n // 2):
        if s[i] == s[n - i - 1]:
            if s[i] == '.':
                s[i] = 'a'
                s[n - i - 1] = 'a'
            else:
                continue
        elif s[i] == '.':
            s[i] = s[n - i - 1]
        elif s[n - i - 1] == '.':
            s[n - i - 1] = s[i]
        else:
            s = -1
            break
    if s != -1:
        s = ''.join(s)
    print(s)
