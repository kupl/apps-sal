def row_weights(array):
    """
    Returns a tuple of total weights for 'team 1' and 'team 2,' where
    the first person of array is in team 1, the second team 2, the third
    in team 1, etc...

    Args:
        array: List of at least two positive integers, which represents 
        peoples' weights.
    Returns:
        tuple of total weights of team 1 and 2.
    """
    weight_t1 = sum((array[i] for i in range(0, len(array), 2)))
    weight_t2 = sum((array[i] for i in range(1, len(array), 2)))
    return (weight_t1, weight_t2)
