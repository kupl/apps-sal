import math


def f(x):
    if x < 10:
        return x
    n = 0
    while x > 0:
        n += x % 10
        x /= 10
    return f(n)


def ans(a, d, n):
    s = 0
    if d == 0:
        print(a * n)
    elif d == 1 or d == 2 or d == 4 or (d == 5) or (d == 7) or (d == 8):
        if n < 9:
            while n > 0:
                s = s + a
                a = f(a + d)
                n = n - 1
            print(s)
        else:
            x = 9
            while x > 0:
                s = s + a
                a = f(a + d)
                x = x - 1
            s = s * int(n / 9)
            n = n % 9
            while n > 0:
                s = s + a
                a = f(a + d)
                n = n - 1
            print(s)
    elif d == 3 or d == 6:
        if n < 3:
            while n > 0:
                s = s + a
                a = f(a + d)
                n = n - 1
            print(s)
        else:
            x = 3
            while x > 0:
                s = s + a
                a = f(a + d)
                x = x - 1
            s = s * int(n / 3)
            n = n % 3
            while n > 0:
                s = s + a
                a = f(a + d)
                n = n - 1
            print(s)
    elif a == 0:
        print(9 * (n - 1))
    else:
        print(a * n)


t = int(input())
while t > 0:
    (a, d, l, r) = list(map(int, input().split(' ')))
    n = r - l + 1
    a = a + (l - 1) * d
    a = f(a)
    d = f(d)
    ans(a, d, n)
    t -= 1
