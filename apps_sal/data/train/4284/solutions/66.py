def array_leaders(numbers):
    """
    Returns 'leader' integers from a list of integers.
    Leader integers are integers that are greater than
    the sum of all the integers to its right.

    Args:
        numbers: A list that has at least 3 integers.
    Returns:
        Leader integers.
    """
    return [x for i, x in enumerate(numbers) if x > sum(numbers[i + 1:])]
