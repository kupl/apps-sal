from typing import Any, List

def filter_homogenous(arrays: List[Any]) -> List[Any]:
    """
    Get a new array which carries over only those arrays from the original, 
    which were not empty and whose items are all of the same type (i.e. homogenous).
    """
    return list(filter(lambda _: len(_) and len(set(map(type, _))) == 1, arrays))
