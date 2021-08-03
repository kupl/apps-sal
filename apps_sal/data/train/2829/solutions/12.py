from typing import List


def array_madness(a: List[int], b: List[int]) -> bool:
    """
    Return `true` if the sum of the squares of each element in `a` 
    is strictly greater than the sum of the cubes of each element in `b`.
    """
    return sum(map(lambda _: pow(_, 2), a)) > sum(map(lambda _: pow(_, 3), b))
