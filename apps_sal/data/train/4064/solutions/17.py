from typing import List

def count_by(x: int, n: int) -> List[int]:
    """ Return a sequence of numbers counting by `x` `n` times. """
    return list(range(x, x * n + 1, x))
