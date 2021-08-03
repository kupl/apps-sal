import math
n = int(input())
tmp = int(math.sqrt(n))
l, r = max(1, n - tmp + 1), n
while True:
    for i in range(l, r + 1):
        print(i, end=' ')
    if l == 1:
        break
    l, r = max(1, l - tmp), l - 1
