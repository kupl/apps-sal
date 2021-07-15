def divisors(n):
    divisor = 1
    count = 0
    while n > divisor:
        if n % divisor == 0:
            count += 1
            divisor += 1
        else:
            divisor += 1
    count += 1
    return count
