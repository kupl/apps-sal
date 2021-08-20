import sys
import math
from collections import defaultdict, Counter
input = sys.stdin.readline


def print(x):
    sys.stdout.write(str(x) + '\n')


t = int(input())
for i in range(t):
    (a, b, n) = map(int, input().split())
    c = a ^ b
    c1 = bin(c).lstrip('0b')
    c1 = list(c1.rjust(max(len(bin(a)), len(bin(b))) - 2, '0'))
    for j in range(len(c1)):
        if c1[j] == '0':
            c1[j] = '1'
        else:
            c1[j] = '0'
    c1 = int(''.join(c1), 2)
    l = [a, b, max(c, c1)]
    ans = l[(n - 1) % 3]
    print(ans)
