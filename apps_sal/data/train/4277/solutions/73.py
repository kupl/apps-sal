from typing import List, Tuple


def difference_in_ages(ages: List[int]) -> Tuple[int, int, int]:
    return min(ages), max(ages), max(ages) - min(ages)
