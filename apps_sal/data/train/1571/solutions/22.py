from fractions import Fraction
for i in range(int(input())):
    a = [int(x) for x in input().split()]
    n = a[0]
    A = a[1]
    k = a[2]
    q = A + (k - 1) / (n - 1) * (360 * (n - 2) / n - 2 * A)
    x = 1
    if q - int(q) < 1 and q - int(q) > 0:
        o = Fraction(q).limit_denominator()
        print(o.numerator, o.denominator)
    else:
        print(int(q), 1)
