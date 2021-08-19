from decimal import *


def firstkdigits(n, k):
    n = Decimal(n)
    product = n * n.log10()
    decimal_part = product % 1
    d = pow(10, decimal_part + k - 1)
    return str(int(d))


for _ in range(int(input())):
    (n, k) = map(int, input().split())
    q2 = str(pow(n, n, 10 ** k)).zfill(k)
    if n >= 1000:
        q1 = firstkdigits(n, k)
    else:
        q1 = str(n ** n)[:k]
    print(q1 + ' ' + q2)
