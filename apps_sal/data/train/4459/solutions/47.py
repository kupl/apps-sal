def nth_even(n):
    if n == 3:
        return 4
    else:
        return (n//2) * 2 if n < 3 else (n * 2) - 2
