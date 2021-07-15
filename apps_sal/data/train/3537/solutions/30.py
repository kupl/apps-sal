def is_even(n): 
    return False if isinstance(n, float) else not bool(n % 2)
