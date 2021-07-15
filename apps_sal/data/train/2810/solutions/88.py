from typing import List
from string import ascii_lowercase


def solve(arr: List[str]) -> List[int]:
    return [sum(c == i for i, c in zip(ascii_lowercase, a.lower())) for a in arr]

