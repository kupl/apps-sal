import sys
import math
from collections import defaultdict


def is_pal(s):
    i, j = 0, len(s) - 1
    while i <= j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


s = sys.stdin.readline()[:-1]
n = len(s)
# print(n,'n')
if n % 2 == 0:
    z = True
    for i in range(n // 2 - 1):
        if s[i] != s[i + 1]:
            z = False
            break
    if z:
        print('Impossible')
    else:
        for i in range(n // 2):
            # print(s[i+1:]+s[:i+1])
            if is_pal(s[i + 1:] + s[:i + 1]) and s[i + 1:] + s[:i + 1] != s:
                print(1)
                return
        print(2)
else:
    z = True
    for i in range(n // 2 - 1):
        if s[i] != s[i + 1]:
            z = False
            break
    if z:
        print('Impossible')
    else:
        print(2)
