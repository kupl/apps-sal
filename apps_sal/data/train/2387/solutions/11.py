import math
import collections
import sys
input = sys.stdin.readline


def case():
    s = int(input())
    ans = 0
    while s:
        spend = (s // 10) * 10
        if spend == 0:
            spend = s
        ans += spend
        back = spend // 10
        s -= spend
        s += back
    print(ans)


for _ in range(int(input())):
    case()
