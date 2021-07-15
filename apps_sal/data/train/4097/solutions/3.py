def reverse_list(x):
    """
    >>> reverse_list([1,2,3])
    [3, 2, 1]
    
    >>> reverse_list([2,3])
    [3, 2]
    """ 
    return x[::-1]

def sum_list(x):
    """
    >>> sum_list([1,2,3])
    6
    
    >>> sum_list([0])
    0
    """
    return sum(x)

def head_of_list(x):
    """
    >>> head_of_list([0])
    0
    
    >>> head_of_list([1,2,3])
    1
    """ 
    return x[0] if x else None
