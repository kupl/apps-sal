def multiple_of_index(arr):
    return [x for (i, x) in enumerate(arr) if i and x % i == 0]
