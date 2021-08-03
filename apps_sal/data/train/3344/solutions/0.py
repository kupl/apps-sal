import math


def number_property(n):
    return [isPrime(n), isEven(n), isMultipleOf10(n)]
    # Return isPrime? isEven? isMultipleOf10?
    # your code here


def isPrime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def isEven(n):
    return n % 2 == 0


def isMultipleOf10(n):
    return n % 10 == 0
