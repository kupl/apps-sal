def factorial(n): return 1 if n == 0 else n * factorial(n - 1)


def strong_num(n):
    if sum(factorial(int(n)) for n in str(n)) == n:
        return "STRONG!!!!"
    return "Not Strong !!"
