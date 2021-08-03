from operator import mul, sub
from typing import List


def find_difference(a: List[int], b: List[int]) -> int:
    """
    Find the difference of the cuboids' volumes regardless of which is bigger
    based on two lists of integers `a` and `b` which representing the dimentions
    of cuboids `a` and `b`.
    """
    return abs(sub(*list(map(lambda x, y, z: x * y * z, *zip(a, b)))))
