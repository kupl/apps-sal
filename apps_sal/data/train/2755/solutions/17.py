from typing import List


def multiple_of_index(arr: List[int]) -> List[int]:
    """ Get a new array consisting of elements which are multiple of their own index in input array. """
    return list(dict(filter(lambda _it: _it[0] > 0 and (_it[1] / _it[0]).is_integer(), enumerate(arr))).values())
