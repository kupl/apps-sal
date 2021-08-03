from typing import List


def create_array(n: int) -> List[int]:
    """ Fix the unfinished loop. """
    result = []
    ix = 1
    while ix <= n:
        result.append(ix)
        ix += 1
    return result
