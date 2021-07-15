def is_even(n): 
    return False if type(n) == float else not abs(n) % 2
