import math


def isprime(n):
    if n <= 1 or n % 2 == 0:
        print(1)
        return False
    if n == 2:
        print(2)
        return True
    for i in range(3, math.floor(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def gap(g, m, n):
    (i, li) = (m, [])
    while i <= n:
        if isprime(i):
            li.append(i)
        if len(li) > 1:
            if li[-1] - li[-2] == g:
                return [li[-2], li[-1]]
        i = i + 1
    return
