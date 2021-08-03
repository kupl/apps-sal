def reverse_list(x):
    """"Takes an list and returns the reverse of it. 
    If x is empty, return [].

    Your two Doc_tests go here... 
    >>> reverse_list([])
    []
    >>> reverse_list([2,3,9])
    [9, 3, 2]
    """
    return x[::-1]


def sum_list(x):
    """Takes a list, and returns the sum of that list.
    If x is empty list, return 0.

    Your two Doc_tests go here...
    >>> sum_list([])
    0
    >>> sum_list([2,3,9])
    14
    """
    return sum(x)


def head_of_list(x):
    """Takes a list, returns the first item in that list.
    If x is empty, return None

    Your two Doc_tests go here...
    >>> head_of_list([5,4,9])
    5
    >>> head_of_list([2,3,9])
    2
    """
    if x == []:
        pass
    else:
        return x[0]
