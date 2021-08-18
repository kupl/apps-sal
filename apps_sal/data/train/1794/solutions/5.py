def is_prime(n):
    if n == 2:
        return True
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            return False
    return True


def factor(n):
    res = []
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            res.append((i, n // i))
    return res


def statement1(s):
    if s % 2 == 0:
        return False
    elif is_prime(s - 2):
        return False
    else:
        return True


def statement2(p):
    factors = factor(p)
    count = 0
    for (f1, f2) in factors:
        tests = [(f1 + f2) % 2 != 0, not is_prime(f1 + f2 - 2), not (is_prime(f1) and is_prime(f2))]
        if all(tests):
            count += 1
    return count == 1


def statement3(s):
    if not statement1(s):
        return False
    pairs = [(x, s - x) for x in range(2, s // 2)]
    count = 0
    for p1, p2 in pairs:
        if statement2(p1 * p2):
            count += 1
    return count == 1


def is_solution(a, b):
    return all([statement1(a + b), statement2(a * b), statement3(a + b)])
