def is_even(n): 
    # your code here
    if type(n) == float:
        return False
    if type(n) == int:
        if n%2 == 0:
            return True
        if n%2 == 1:
            return False
