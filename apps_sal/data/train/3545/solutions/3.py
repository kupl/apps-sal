from itertools import chain
from typing import List, Any


def well(arr: List[List[Any]]) -> str:
    good = (a for a in chain(*arr) if isinstance(a, str) and a.lower() == "good")
    
    if next(good, False):
        if next(good, False) and next(good, False):
            return "I smell a series!"
        return "Publish!"
    return "Fail!"

