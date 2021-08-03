def min_sum(arr):
    """
    Returns the minimum sum nof integer products of arr.
    """
    return min_sum_helper(sorted(arr))


def min_sum_helper(arr):
    """
    Recursive helper method for min_sum.
    """
    if len(arr) == 2:
        return arr[0] * arr[-1]
    return (arr[0] * arr[-1]) + min_sum_helper(arr[1:-1])
