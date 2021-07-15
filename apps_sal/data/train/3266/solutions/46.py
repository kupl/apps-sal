from contextlib import suppress

def my_first_kata(a, b):
    if type(a) == type(b) == int: 
        with suppress(ZeroDivisionError):
            return a % b + b % a
    return False
