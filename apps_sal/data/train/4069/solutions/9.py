# Using Binet's Formula to speed things up
def nth_fib(n):
    Phi = (pow(5, 0.5) + 1) / 2
    phi = Phi - 1
    n -= 1
    return round((pow(Phi, n) - pow(-phi, n)) / pow(5, 0.5))
