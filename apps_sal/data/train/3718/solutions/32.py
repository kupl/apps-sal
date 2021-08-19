def divisors(n):
    return len([num for num in range(1, n + 1) if not n % num])
