def solve(n):
    return n if n < 10 else 9 + solve(n // 10) if n % 10 == 9 else 10 + n % 10 + solve(n // 10 - 1)
