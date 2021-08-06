import sys
import math
n = int(input())
k = [int(x) for x in sys.stdin]
size = (5 * 10**5 + 4)
r = [0] * size
c = [0] * size
for i in k:
    r[i // 2] += 1  # neu co so = x2 -> +1
    c[i] += 1  # dem so lan xuat hien trong input
t = b = 0
result = n
for i in range(size - 1, -1, -1):
    r[i] += t
    t = r[i]
    if (c[i] > 0):
        result -= min(c[i], r[i] - b)
        b += min(c[i], r[i] - b)
    if (result <= ((n + 1) // 2)):
        break
print(max(result, (n + 1) // 2))
