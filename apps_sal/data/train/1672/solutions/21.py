import sys
import math

for nraw in sys.stdin.read().strip().split('\n')[::-1]:
    n = int(nraw)
    res = n ** 3 * 5 + math.sqrt(abs(n))
    if res > 400:
        print('f(%d) = MAGNA NIMIS!' % n)
    else:
        print('f(%d) = %.2f' % (n, res))

