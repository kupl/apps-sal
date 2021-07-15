from typing import Tuple

def lovefunc(*flowers: Tuple[int]) -> bool:
    """ Are Timmy & Sarah in love? """
    return len(list(filter(lambda _it: _it % 2, flowers))) == 1
