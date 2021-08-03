def is_even(n):
    if type(n) == float:
        return False
    if n % 2 == 0:
        return True
    return False
