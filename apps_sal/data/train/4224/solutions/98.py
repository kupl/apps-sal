def dont_give_me_five(start, end):
    """
    returns the number of numbers in the range of starts -> end 
    that dont include a 5
    input: int,int
    output: int
    >>> dont_give_me_five(-11,10)
    >>> 20
    """
    n = 0
    for i in range(start, end + 1):
        if '5' not in str(i):
            n += 1
    return n
