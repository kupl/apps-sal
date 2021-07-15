from functools import reduce
from operator import ixor
from typing import List

def logical_calc(array: List[bool], op: str) -> bool:
    """ Calculate logical value of boolean array. """
    return {
        "AND": lambda: all(array),
        "OR": lambda: any(array),
        "XOR": lambda: reduce(ixor, array)
    }.get(op)()
