from decimal import Decimal
for _ in range(0, eval(input())):
    ([r1, h1, r2, h2], p) = (list(map(Decimal, input().split())), Decimal(3.141592653589793))
    print(p * r1 ** 2 * (h1 + Decimal(2.0) * r1) / 3, p * r2 ** 2 * h2)
