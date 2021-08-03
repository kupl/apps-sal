import math


def i1():
    return int(input())


def i2():
    return [int(i) for i in input().split()]


q = i1()
y = []
for i in range(q):
    y.append(i2())

for a, b in y:
    x = a * b
    c = int(math.sqrt(x))
    if c**2 == x:
        c -= 1
    z = 2 * c
    if c > 0 and (x // c) == c:
        z -= 1
    if c > 0 and x % c == 0 and (x // c - 1) == c:
        z -= 1
    if a <= c:
        z -= 1
    if b <= c:
        z -= 1
    print(z)
