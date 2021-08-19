import sys
import math
n = int(input())
k = sorted((int(x) for x in sys.stdin))
p1 = n // 2 - 1
p2 = n - 1
count = 0
while p2 > n // 2 - 1 and p1 >= 0:
    if k[p1] * 2 <= k[p2]:
        p2 -= 1
        count += 1
    p1 -= 1
print(n - count)
