def reverse_list(x):
    """Takes an list and returns the reverse of it. 
    If x is empty, return [].

    >>> reverse_list([1, 2, 3, 4])
    [4, 3, 2, 1]
    >>> reverse_list([])
    []
    """
    return x[::-1]


def sum_list(x):
    """Takes a list, and returns the sum of that list.
    If x is empty list, return 0.

    >>> sum_list([1, 2, 3, 4])
    10
    >>> sum_list([])
    0
    """
    return sum(x)


def head_of_list(x):
    """Takes a list, returns the first item in that list.
    If x is empty, return None

    >>> head_of_list([1, 2, 3, 4])
    1
    >>> head_of_list([]) is None
    True
    """
    return x[0] if x else None
