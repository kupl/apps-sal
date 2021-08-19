from math import sqrt
l = []
for i in range(11):
    l.append(int(input()))
for v in reversed(l):
    x = int(v)
    ans = 5 * x ** 3 + sqrt(abs(x))
    if ans > 400:
        print(str.format('f({}) = MAGNA NIMIS!', x))
    else:
        print(str.format('f({}) = {:.2f}', x, ans))
