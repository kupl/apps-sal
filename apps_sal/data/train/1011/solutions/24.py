import collections
from collections import defaultdict
import math


def chef(s, c, k):
    if c <= k:
        return True
    else:
        return False


def brother(s, c, k):
    if s <= k:
        return True
    else:
        return False


for _ in range(int(input())):
    (n, k) = [int(x) for x in input().split()]
    s = input()
    cap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    small = cap.lower()
    ss = 0
    for x in s:
        if x in small:
            ss += 1
    cc = n - ss
    ch = chef(ss, cc, k)
    bro = brother(ss, cc, k)
    if ch and bro:
        print('both')
    elif ch and (not bro):
        print('chef')
    elif not ch and bro:
        print('brother')
    else:
        print('none')
