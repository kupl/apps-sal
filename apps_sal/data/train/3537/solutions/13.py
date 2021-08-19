def is_even(n):
    if type(n) != int:
        return False
    elif n % 2 == 1:
        return False
    else:
        return True
