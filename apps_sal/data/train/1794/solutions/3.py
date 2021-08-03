from functools import reduce


def isPrime(n):
    d = 2

    while True:
        if n % d == 0:
            return False
        if d * d > n:
            return True
        d += 1


def primeFactor(n):
    d = 2
    factors = []
    while True:
        if n % d == 0:
            factors.append(d)
            n = n // d
        else:
            d += 1

        if n == 1:
            return factors
        elif d * d > n:
            return factors + [n]


def get_cases(nums):
    nums_plus = list(map(lambda x: x + 1, nums))
    total_cases = reduce(lambda x, y: x * y, nums_plus)

    for i in range(total_cases):
        v = i
        cases = []
        for n in nums_plus:
            cases.append(v % n)
            v = v // n
        yield(cases)


def statement1(s):
    if s % 2 == 0:
        return False
    return not isPrime(s - 2)


def statement2(p):
    factors = primeFactor(p)

    if len(factors) == 2:
        return False

    factors_set = set(factors)
    factor_tuples = []
    for factor in factors_set:
        factor_tuples.append((factor, factors.count(factor)))

    sum_set = set()
    nums = [x[1] for x in factor_tuples]
    for case in get_cases(nums):
        v1 = v2 = 1
        if sum(case) == 0 or sum(case) == len(factors):
            continue

        for i, n in enumerate(case):
            v1 *= factor_tuples[i][0] ** (factor_tuples[i][1] - n)
            v2 *= factor_tuples[i][0] ** n

        sum_set.add(v1 + v2)

    if sum([statement1(x) for x in sum_set]) == 1:
        return True
    return False


def statement3(s):
    if statement1(s) == False:
        return False

    if sum([statement2(x * (s - x)) for x in range(2, s // 2 + 1)]) == 1:
        return True
    return False


def is_solution(a, b):
    return statement3(a + b)
