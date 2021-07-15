def is_even(n): 
    if isinstance(n, float):
        return False
    else:
        return not (n % 2)
