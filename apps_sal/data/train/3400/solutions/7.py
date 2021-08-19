from typing import List


def even_numbers(arr: List[int], n: int) -> List[int]:
    res = []
    for a in reversed(arr):
        if a % 2 == 0:
            res.insert(0, a)
            if len(res) == n:
                return res
