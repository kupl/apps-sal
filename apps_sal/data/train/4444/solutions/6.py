def abundant_number(n):
    return sum((n // i + i for i in range(2, int(n ** 0.5) + 1) if n % i == 0)) + 1 > n
