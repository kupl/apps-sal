def dont_give_me_five(start, end):
    '''
    returns the number of numbers in the range of starts -> end 
    that dont include a 5
    input: int,int
    output: int
    >>> dont_give_me_five(-11,10)
    >>> 20
    '''
    # initialize return n
    n = 0

    # iterate through numbers
    for i in range(start, end + 1):

        # check for '5' in str(int)
        if '5' not in str(i):
            n += 1

    return n   # amount of numbers
