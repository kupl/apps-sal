import math
import sys
n = int(input())
k = n
a = sorted([int(x) for x in sys.stdin.read().strip().split('\n')])
p1 = math.floor((n - 1) / 2)
p2 = n - 1
while p1 >= 0:
    if 2 * a[p1] <= a[p2]:
        k -= 1
        a[p2] = 0
        p2 -= 1
    p1 -= 1
k = max(math.ceil(n / 2), k)
sys.stdout.write(str(k))
