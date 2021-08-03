def is_prime(n):
    return n == 2 or n % 2 != 0 and all(n % k != 0 for k in range(3, root(n) + 1, 2))


def root(p):
    return int(p ** 0.5)


def statement1(s):
    return not(s % 2 == 0 or is_prime(s - 2))


def statement2(p):
    return sum(statement1(i + p / i) for i in range(2, root(p) + 1) if p % i == 0) == 1


def statement3(s):
    return sum(statement2(i * (s - i)) for i in range(2, s / 2 + 1)) == 1


def is_solution(a, b):
    return statement1(a + b) and statement2(a * b) and statement3(a + b)
