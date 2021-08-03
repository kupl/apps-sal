from typing import List, Optional


def first_non_consecutive(arr: List[int]) -> Optional[int]:
    """ Find the first element of an array that is not consecutive. """
    for prev, next in zip(arr, arr[1:]):
        if next - prev > 1:
            return next
