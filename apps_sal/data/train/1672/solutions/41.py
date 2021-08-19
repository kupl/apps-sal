import math
res = list()
for i in range(11):
    n = int(input())
    p = math.sqrt(math.fabs(n)) + n ** 3 * 5
    res.append((n, p))
for (k, v) in res[::-1]:
    if v < 400:
        print('f(%d) = %.2f' % (k, v))
    else:
        print('f(%d) = MAGNA NIMIS!' % k)
