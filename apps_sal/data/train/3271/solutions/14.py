from typing import List, Tuple, Optional


def arr(*args: Optional[Tuple[int]]) -> List[int]:
    """ Get an array with the numbers 0 to N-1 in it. """
    return list(range(0, *args))
