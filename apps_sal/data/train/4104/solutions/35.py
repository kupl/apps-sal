def max_tri_sum(numbers):
    """
    Return the maximum triplet sum in numbers without duplications.
    
    Args:
        numbers: List of at least three integers.
    Returns:
        maximum triplet sum.
    """
    lst = sorted(list(set(numbers)))
    return sum(lst[len(lst) - 3:])
