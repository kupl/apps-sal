# This function should return n!
def factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        factorial = 1
        for val in xrange(1, n + 1):
            factorial *= val
        return factorial
