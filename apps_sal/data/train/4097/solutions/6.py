def reverse_list(a):
    """Takes an list and returns the reverse of it. 
    If x is empty, return [].

    >>> reverse_list([1])
    [1]
    >>> reverse_list([])
    []
    """
    return a[::-1]


def sum_list(a):
    """Takes a list, and returns the sum of that list.
    If x is empty list, return 0.

    >>> sum_list([1])
    1
    >>> sum_list([])
    0
    """
    return sum(a)


def head_of_list(a):
    """Takes a list, returns the first item in that list.
    If x is empty, return None

    >>> head_of_list([1])
    1
    >>> head_of_list([]) is None
    True
    """
    if a:
        return a[0]
