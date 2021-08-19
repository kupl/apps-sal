def max_number(n):
    """function to determine the largest value given a array of numbers. It will convert them to a string, sort them in descending order and then return the list as an int"""
    if not isinstance(n, int):
        raise TypeError("Sorry, I'm expecting an int")
    if n < 0:
        raise ValueError("Sorry, 'n' needs to be larger than 1")
    return int(''.join(sorted(list(str(n)), reverse=True)))
