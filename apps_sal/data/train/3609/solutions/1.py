from typing import List


def is_onion_array(a: List[int]) -> bool:
    return all(aj + ak <= 10 for aj, ak in zip(a, a[:(len(a) - 1) // 2:-1]))
