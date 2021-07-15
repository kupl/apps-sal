def fusc(n):
    return n if n <= 1 else fusc(n / 2) + (fusc(n / 2 + 1) if n % 2 == 1 else 0)
