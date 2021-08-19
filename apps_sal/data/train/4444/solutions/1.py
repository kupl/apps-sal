def abundant_number(n):
    return sum((m for m in range(1, n) if n % m == 0)) > n
