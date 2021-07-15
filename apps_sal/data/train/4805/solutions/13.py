from typing import List, Union

def check(seq: List[Union[int, str]], elem: Union[int, str]) -> bool:
    """ Check if the element is in the array. """
    return elem in seq
