from typing import List

def divisible_by(numbers: List[int], divisor: int) -> List[int]:
    """ Get all numbers which are divisible by the given divisor. """
    return list(filter(lambda it: not it % divisor, numbers))
