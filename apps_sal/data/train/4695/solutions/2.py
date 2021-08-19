def count_squares(n):
    """ Function that uses recursion to calculate the number of square units in an n X n square"""
    if n == 1:
        return 1
    else:
        return n ** 2 + count_squares(n - 1)
