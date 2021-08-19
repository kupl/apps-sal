import sys


def check(a, b, c, d):
    return a == c and b == d or (a == d and b == c)


(a, b, c, d) = list(map(int, sys.stdin.readline().split()))


def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)


flag = False
(lg0, rg0) = (gcd(a, b), gcd(c, d))
if check(a / lg0, b / lg0, c / rg0, d / rg0):
    flag = True
(lg0, rg0) = (gcd(a, c), gcd(b, d))
if check(a / lg0, c / lg0, b / rg0, d / rg0):
    flag = True
(lg0, rg0) = (gcd(a, d), gcd(c, b))
if check(a / lg0, d / lg0, c / rg0, b / rg0):
    flag = True
print('Possible' if flag else 'Impossible')
