from sys import stdin, stdout
from math import floor, ceil
n = int(input())
a = sorted(list((int(stdin.readline()) for i in range(n))))
mid = floor((n - 1) / 2)
c = 0
i = n - 1
x = mid
k = n
while x >= 0:
    if 2 * a[x] <= a[i]:
        k -= 1
        i -= 1
    x -= 1
k = max(ceil(n / 2), k)
stdout.write(str(k))
