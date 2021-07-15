from collections import Counter
from typing import List


def check_three_and_two(array: List[str]) -> bool:
    return set(Counter(array).values()) == {2, 3}

