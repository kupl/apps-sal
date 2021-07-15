from typing import List, Union

def count_by(x: Union[int,float], n: int) -> List[Union[int,float]]:
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    return [x*it for it in range(1,n+1)]

