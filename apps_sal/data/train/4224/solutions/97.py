def dont_give_me_five(start,end):
    '''
    returns the number of numbers in the range of starts -> end 
    that dont include a 5
    input: int,int
    output: int
    >>> dont_give_me_five(-11,10)
    >>> 20
    '''
    # list comprehension
    # sum( all of the trues which turn into 1's)
    return sum('5' not in str(i) for i in range(start,end+1))
