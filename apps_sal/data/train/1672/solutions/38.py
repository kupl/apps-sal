from math import sqrt


def f(x):
    return sqrt(abs(x))


def g(x):
    return x ** 3 * 5


arr = []
for _ in range(11):
    arr.append(int(input()))
arr.reverse()
for e in arr:
    r = f(e) + g(e)
    if 400 < r:
        print('f(%d) = ' % e + 'MAGNA NIMIS!')
        continue
    print('f(%d) = %.2f' % (e, r))
