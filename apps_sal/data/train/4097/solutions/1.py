def reverse_list(lst):
    """Takes an list and returns the reverse of it. 
    If x is empty, return [].
    >>> reverse_list([])
    []
    >>> reverse_list([1, 2, 3])
    [3, 2, 1]
    """ 
    return lst[::-1]

def sum_list(lst):
    """Takes a list, and returns the sum of that list.
    If x is empty list, return 0.
    >>> sum_list([])
    0
    >>> sum_list([1, 2, 3])
    6
    """
    return sum(lst)

def head_of_list(lst):
    """Takes a list, returns the first item in that list.
    If x is empty, return None
    >>> head_of_list([]) is None
    True
    >>> head_of_list([1, 2, 3])
    1
    """
    return lst[0] if lst else None
