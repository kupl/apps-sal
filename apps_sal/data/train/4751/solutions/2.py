def pdsum(n):
    """proper divisors sum"""
    xs = {1}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            xs.add(i)
            xs.add(n // i)
    return sum(xs)


def describe(s, n):
    if s < n:
        return 'deficient'
    elif s > n:
        return 'abundant'
    else:
        return 'perfect'


def deficiently_abundant_amicable_numbers(n1, n2):
    (s1, s2) = (pdsum(n) for n in [n1, n2])
    return '{} {} {}'.format(describe(s1, n1), describe(s2, n2), 'amicable' if s1 == n2 and s2 == n1 and (n1 != n2) else 'not amicable')
