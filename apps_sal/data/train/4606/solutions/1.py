import re


def valid_romans(arr):
    """Return all elements of 'arr' which are correct Roman numbers between 1 and 4999."""
    return [roman for roman in arr if roman and re.fullmatch(
        "(M{,4})"
        "(C[MD]|D?C{,3})"
        "(X[CL]|L?X{,3})"
        "(I[XV]|V?I{,3})", roman)]
