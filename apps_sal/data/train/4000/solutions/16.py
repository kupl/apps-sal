def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


def strong_num(n):
    factorial_sum = sum((factorial(int(n)) for n in str(n)))
    return 'STRONG!!!!' if factorial_sum == n else 'Not Strong !!'
