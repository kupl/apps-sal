from typing import List


def bar_triang(a: List[int], b: List[int], c: List[int]) -> List[float]:
    return [round((a[0] + b[0] + c[0]) / 3, 4), round((a[1] + b[1] + c[1]) / 3, 4)]

