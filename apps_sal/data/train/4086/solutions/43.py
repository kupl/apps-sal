def first_non_consecutive(arr):
    return next((n for i, n in enumerate(arr[1:]) if n != arr[i] + 1), None)
    """ WARNING: i = 0 for the second element of arr! ;) """
