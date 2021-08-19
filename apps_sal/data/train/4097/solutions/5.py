def reverse_list(x):
    """Takes an list and returns the reverse of it. 
    If x is empty, return [].

    >>> reverse_list([1, 2, 3])
    [3, 2, 1]
    >>> reverse_list([])
    []
    """
    return x[::-1] if x else []


def sum_list(x):
    """Takes a list, and returns the sum of that list.
    If x is empty list, return 0.
    >>> sum_list([1, 2, 3])
    6
    >>> sum_list([])
    0
    """
    return sum(x) if x else 0


def head_of_list(x):
    """Takes a list, returns the first item in that list.
    If x is empty, return None

    >>> head_of_list([1, 2])
    1
    >>> head_of_list([]) is None
    True
    """
    return x[0] if x else None
