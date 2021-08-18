""" isdiv works thusly:
Create a function isDivisible(n, x, y)
that checks if a number n is divisible
by two numbers x AND y. All inputs are
positive, non-zero digits.
"""


def is_divisible(n, x, y):
    """is divisible checks if a number n is divisible
    by two numbers x AND y. All inputs are
    positive, non-zero digits.

    >>> is_divisible(3,1,3)
    True
    >>> is_divisible(12,2,6)
    True
    >>> is_divisible(100,5,3)
    False
    >>> is_divisible(12,7,5)
    False

    >>> is_divisible(0,1,1)
    Traceback (most recent call last):
     ...
    ValueError: Must be integer greater than 0
    >>> is_divisible(1,0,1)
    Traceback (most recent call last):
     ...
    ValueError: Must be integer greater than 0
    >>> is_divisible(1,1,0)
    Traceback (most recent call last):
     ...
    ValueError: Must be integer greater than 0
    """

    if n < 1 or x < 1 or y < 1:
        raise ValueError('Must be integer greater than 0')

    return n % x == 0 and n % y == 0
