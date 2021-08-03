from sys import stdin
from fractions import Fraction

input = stdin.readline

for _ in range(int(input())):
    a, b, n = list(map(int, input().split()))
    ab = Fraction(a, b)

    p = set()

    for i in range(1, n + 1):
        for j in range(n, 0, -1):
            x = Fraction(i, j)

            if x > ab:
                break

            p.add(x)

    x = sorted(p)[-2]

    print(x.numerator, x.denominator)
