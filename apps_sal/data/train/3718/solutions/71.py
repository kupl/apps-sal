def divisors(n):
    sum = 0
    for numbers in range(1, n + 1):
        if n % numbers == 0:
            sum += 1
    return sum
