from collections import OrderedDict
from typing import List


def solve(arr: List[int]) -> List[int]:
    d = OrderedDict()
    for a in arr:
        try:
            d.move_to_end(a)
        except KeyError:
            d[a] = None

    return list(d.keys())

