from copy import deepcopy


def remove_smallest(numbers):
    if not numbers:
        return numbers
    n = deepcopy(numbers)
    n.remove(min(numbers))
    return n
