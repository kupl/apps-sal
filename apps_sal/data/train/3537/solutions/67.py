def is_even(n): 
    while n > 0 or n < 0:
        if n % 2 == 0:
            return True
        else:
            return False
    if n == 0:
        return True

