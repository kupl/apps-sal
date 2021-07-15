def collatz(n):
    return 1 if n == 1 else 1 + collatz(3 * n + 1 if n % 2 else n // 2)
