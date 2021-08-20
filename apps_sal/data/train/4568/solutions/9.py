from functools import reduce
from typing import List, Optional, Tuple


def find_min_max_product(arr: List[int], kpi: int) -> Optional[Tuple[int, int]]:
    if kpi <= len(arr):
        mul = []
        arr.sort()
        for _ in range(kpi):
            mul.append(reduce(lambda x, y: x * y, arr[0:kpi], 1))
            mul.append(reduce(lambda x, y: x * y, arr[-kpi:], 1))
            arr = [arr[-1]] + arr[:-1]
        return (min(mul), max(mul))
    return None
