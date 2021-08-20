def deficiently_abundant_amicable_numbers(n1, n2):
    (d1, d2) = (sum((d for d in range(1, n // 2 + 1) if n % d == 0)) for n in (n1, n2))
    is_amicable = 'not ' if n1 == n2 or (n1, n2) != (d2, d1) else ''
    return f'{perfection(n1, d1)} {perfection(n2, d2)} {is_amicable}amicable'


def perfection(n, d):
    return 'deficient' if d < n else 'abundant' if n < d else 'perfect'
