def divisors(n):
    divisors = 0
    for num in range(1, n + 1):
        if n % num == 0:
            divisors += 1
    return divisors
