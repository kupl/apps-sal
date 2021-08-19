from typing import List


def is_sorted_and_how(arr: List[int]) -> str:
    order = (a > b for (a, b) in zip(arr, arr[1:]) if a != b)
    if next(order):
        return 'yes, descending' if all(order) else 'no'
    return 'yes, ascending' if not any(order) else 'no'
