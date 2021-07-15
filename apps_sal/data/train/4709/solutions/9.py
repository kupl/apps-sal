def sequence(n):
    return 3 * sequence(n // 2) + n % 2 if n > 0 else 0
