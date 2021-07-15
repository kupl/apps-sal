def divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n / i % 1 == 0:
            count += 1
    return count
