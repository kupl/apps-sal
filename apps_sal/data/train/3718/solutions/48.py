def divisors(n):
    factors = [num for num in range(1, n // 2 + 1) if n % num == 0]
    return len(factors) + 1
