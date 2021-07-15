import math

def factorial(n):
    try:
        return math.factorial(n)
    except ValueError:
        return None
