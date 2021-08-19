from math import sqrt


def is_prime(x):
    return all((x % y != 0 for y in range(2, int(sqrt(x)) + 1)))


def statement1(s):
    return s % 2 > 0 and (not is_prime(s - 2))


def statement2(p):
    return 1 == sum((p % i == 0 and statement1(i + p // i) for i in range(2, int(sqrt(p)) + 1)))


def statement3(s):
    return 1 == sum((statement2(i * (s - i)) for i in range(2, s // 2 + 1)))


def is_solution(a, b):
    return statement1(a + b) and statement2(a * b) and statement3(a + b)
