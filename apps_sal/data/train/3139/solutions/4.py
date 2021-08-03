from typing import List


def index(array: List[int], n: int) -> int:
    """ Get the N-th power of the element in the array with the index N. """
    try:
        return pow(array[n], n)
    except IndexError:
        return -1
