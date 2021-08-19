import math


def statement1(s):
    if s % 2 == 0:
        return False
    if is_prime(s - 2):
        return False
    return True


def statement2(p):
    if p % 2 != 0:
        return False
    facs = []
    for i in range(2, int(math.sqrt(p)) + 1):
        if p % i == 0:
            facs.append((i, int(p / i)))
    c = 0
    for f in facs:
        if statement1(f[0] + f[1]):
            c += 1
            if c > 1:
                return False
    return c == 1


def statement3(s):
    c = 0
    if not statement1(s):
        return False
    for i in range(2, s // 2):
        if statement2(i * (s - i)):
            c += 1
            if c > 1:
                return False
    return c == 1


def is_solution(a, b):
    return statement1(a + b) and statement2(a * b) and statement3(a + b)


def is_prime(n):
    if n < 2 or (n > 2 and n % 2 == 0):
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
