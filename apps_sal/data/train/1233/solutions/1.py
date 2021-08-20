import sys
import math
from collections import defaultdict, Counter


def possible(n1, n):
    odd = set()
    for j in range(n):
        if s[j] in odd:
            odd.remove(s[j])
        else:
            odd.add(s[j])
        if j < n1 - 1:
            continue
        if len(odd) <= 1:
            return True
        if s[j - n1 + 1] in odd:
            odd.remove(s[j - n1 + 1])
        else:
            odd.add(s[j - n1 + 1])
    return False


t = int(input())
for i in range(t):
    s = input().strip()
    n = len(s)
    ans = 0
    for j in range(n, 0, -1):
        if possible(j, n):
            ans = j
            break
    print(ans)
