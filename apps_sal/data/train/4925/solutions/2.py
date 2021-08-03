def collatz(n):
    return str(n) + '->' + collatz(3 * n + 1 if n % 2 else n / 2) if n != 1 else '1'
