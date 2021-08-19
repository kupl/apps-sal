import sys


def power(a, n, m):
    r = 1
    c = a
    while n:
        if n & 1:
            r = r * c % m
        n >>= 1
        c = c * c % m
    return r


t = int(input())
a = list()
while t:
    n = int(input())
    n = min(n, 33)
    a.append((1 << n) - 1)
    t -= 1
for i in range(len(a)):
    sys.stdout.write('Case ' + str(i + 1) + ': ' + str(a[i]) + '\n')
