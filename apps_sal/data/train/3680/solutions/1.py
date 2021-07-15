def factorial(n):
    if n <= 1:
        if n < 0:
            return None
        else:
            return 1
    return n * factorial(n-1)
