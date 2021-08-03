def divisors(n):
    divisor = 1
    total = 0
    while divisor <= n:
        if n % divisor == 0:
            total += 1
        divisor += 1
    return total
