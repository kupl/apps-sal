import sys
import math

n = int(input())
an = [int(x) for x in (sys.stdin.readline()).split()]

vsum = sum(an)
res = int(vsum / (n - 1))
if(vsum % (n - 1) != 0):
    res += 1

print(max(res, max(an)))
