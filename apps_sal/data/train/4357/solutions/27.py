def nth_smallest(arr, pos):
    """
    Returns the nth smallest integer in arr.
    
    Args:
        arr: List of at least 3 integers.
    Returns:
        Nth smallest integer.
    """
    arr_sorted = sorted(arr)
    return arr_sorted[pos - 1]
