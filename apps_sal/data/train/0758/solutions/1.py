import math


def func(x, b, c):
    ans = x * x + b * x + c
    ans /= math.sin(x)
    return ans


for asd in range(int(input())):
    b, c = map(float, input().split())

    st = 0
    en = math.pi / 2
    iterations = 0
    ans = func(en, b, c)
    while en - st > 0.000001:
        if iterations > 100:
            break

        x1 = st + (en - st) / 3
        x2 = en - (en - st) / 3
        fx1 = func(x1, b, c)
        fx2 = func(x2, b, c)
        if abs(fx2 - fx1) < 0.00000001:
            break
        ans = min(ans, min(fx1, fx2))
        if fx2 < fx1:
            st = x1
        else:
            en = x2

        iterations += 1
    print("%.12f" % ans)
