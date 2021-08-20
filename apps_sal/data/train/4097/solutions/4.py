def reverse_list(x):
    """Takes an list and returns the reverse of it. 
    If x is empty, return [].

    Your two Doc_tests go here... 

     >>> reverse_list([1,2])
     [2, 1]
     >>> reverse_list([])
     []
     """
    return x[::-1]


def sum_list(x):
    """Takes a list, and returns the sum of that list.
    If x is empty list, return 0.

    Your two Doc_tests go here...
    >>> sum_list([])
    0
    >>> sum_list([1,2,3])
    6
    """
    return 0 if len(x) == 0 else sum(x)


def head_of_list(x):
    """Takes a list, returns the first item in that list.
    If x is empty, return None

    Your two Doc_tests go here...
    >>> head_of_list([1,2,3])
    1
    >>> head_of_list([2,4,5])
    2
    """
    return None if len(x) == 0 else x[0]
