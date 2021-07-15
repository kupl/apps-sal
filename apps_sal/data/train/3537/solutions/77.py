def is_even(n):
    result = True

    if type(n) == float or n % 2 != 0:
        result = False

    return result
