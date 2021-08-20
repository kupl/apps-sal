def p(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y & 1:
            res = res * x % p
        y = y >> 1
        x = x * x % p
    return res


def nod(x):
    i = 0
    while x:
        x //= 10
        i += 1
    return i


def ltd(n):
    temp = 1
    for i in range(1, 3):
        temp *= 10
        temp = p(5, n, temp)
    for i in range(2 - nod(temp)):
        print(0, end='')
    if temp:
        print(temp)


def __starting_point():
    n = int(input())
    ltd(n)


__starting_point()
