def sum_str(a, b):
    """
        Returns the sum (as a string) of 'a' and 'b' (also them as a string). 
    """
    return str(sum(map(lambda x: int(x) if x else 0, [a, b])))
