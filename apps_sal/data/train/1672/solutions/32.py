from math import *


def f(n):
    return 5 * n ** 3 + sqrt(abs(n))


e = []
for i in range(11):
    e.append(int(input()))
e.reverse()
for i in e:
    k = f(i)
    if k > 400:
        print('f(%d) = MAGNA NIMIS!' % i)
    else:
        print('f(%d) = %.2f' % (i, k))
