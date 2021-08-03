import sys
import math

n, k = [int(x) for x in (sys.stdin.readline()).split()]
res = []

if(k == 1):
    for i in range(1, n + 1):
        res.append(str(i))
    print(" ".join(res))
    return

z = n
for i in range(n, 1, -1):
    if(i > k):
        res.append(str(i))
    else:
        z = i
        break
l = z
j = 1
for i in range(1, z + 1):
    if(i % 2 != 0):
        res.append(str(j))
        j += 1
    else:
        res.append(str(z))
        z -= 1

print(" ".join(res[::-1]))
