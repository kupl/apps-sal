def is_even(n):
    even = True
    if (n % 2) > 0:
        even = False
        return False
    elif (n % 2) == 0:
        even = True
        return True

