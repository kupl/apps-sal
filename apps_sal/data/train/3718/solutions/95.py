def divisors(n):
    count = 1
    for i in range(1, n // 2 + 1):
        if not n % i:
            count += 1
    return count
