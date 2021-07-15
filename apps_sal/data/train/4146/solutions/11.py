from typing import List


def is_sorted_and_how(arr: List[int]) -> str:
    # Calculate order between consecutively items
    order = (a > b for a, b in zip(arr, arr[1:]) if a != b)

    # Check if the first difference notes a ascending order
    if next(order):
        # Now check if the rest is in descending order
        return "yes, descending" if all(order) else "no"

    # Check if the rest is in ascending order
    return "yes, ascending" if not any(order) else "no"

