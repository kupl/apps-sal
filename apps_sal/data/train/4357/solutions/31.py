from heapq import nsmallest
from typing import List


def nth_smallest(arr: List[int], pos: int) -> int:
    return nsmallest(pos, arr)[-1]
