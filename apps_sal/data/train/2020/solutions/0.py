import math
from functools import reduce

n = int(input())
odd = -1
beads = [int(x) for x in input().split()]
for i in range(n):
    if beads[i] % 2:
        if odd >= 0:
            print(0)
            print(''.join(chr(ord('a') + i) * beads[i] for i in range(n)))
            break
        else:
            odd = i
else:
    gcd = reduce(lambda x, y: math.gcd(x, y), beads)
    print(gcd)
    if odd >= 0:
        s = ''.join(chr(ord('a') + i) * (beads[i] // (2 * gcd)) for i in range(n) if i != odd)
        p = s + chr(ord('a') + odd) * (beads[odd] // gcd) + s[::-1]
        print(p * gcd)
    else:
        s = ''.join(chr(ord('a') + i) * (beads[i] // gcd) for i in range(n))
        p = s + s[::-1]
        print(p * (gcd // 2))
