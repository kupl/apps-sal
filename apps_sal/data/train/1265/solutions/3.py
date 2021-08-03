import math


def answer(n):
    n -= 1
    if n > 0:
        a = int(math.log(n, 5))
    else:
        a = 0
    total = 0
    while a != 0:
        x = math.pow(5, a)
        g = n // x
        n = int(n % x)
        total += 2 * math.pow(10, a) * g
        if n > 0:
            a = int(math.log(n, 5))
        else:
            a = 0
    total += 2 * (n)
    total = int(total)
    return total


T = int(input(''))
while T:
    T -= 1
    n = int(input(''))
    print(answer(n))
