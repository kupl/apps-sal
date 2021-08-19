def is_prime(n):
    if n == 2:
        return True
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:  # no remainder
            return False
    return True


def factor(n):
    res = []
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            res.append((i, n // i))
    return res


def statement1(s):
    # Statement 1: "Patricia cannot know what the two numbers are."
    # so sum is not sum of 2 primes, since goldbach conjecture says
    # all even numbers>3 can be written as sum of 2 primes
    # then sum is not even
    # if sum is even then statement 1 cannot be made
    if s % 2 == 0:
        return False
    # so sum is odd, need to make sure that s-2 is not prime
    elif is_prime(s - 2):
        return False
    # otherwise we are sure s cannot be written as sum of two primes
    else:
        return True


def statement2(p):
    # Statement 2: "In that case, I do know what the two numbers are."
    # a,b not primes but patricia knows the numbers
    # we know that sam's number is odd and cannot be written as 2+prime
    # factor p into pairs of factors and sum the pairs up
    # if sum is even, remove. if sum can be written as 2+prime, remove.
    # if numbers in pair are both prime, remove
    # if left with only one pair -> True; else -> False
    factors = factor(p)
    count = 0
    for (f1, f2) in factors:
        tests = [(f1 + f2) % 2 != 0, not is_prime(f1 + f2 - 2), not (is_prime(f1) and is_prime(f2))]
        if all(tests):
            count += 1
    return count == 1


def statement3(s):
    # s needs to pass statement1 first
    # then, get all pairs of number that sum up to s
    # make sure that only 1 such pair passes statement2
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
