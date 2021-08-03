def first_non_consecutive(arr):
    first, last = arr[0], arr[-1]
    diff = set(range(first, last + 1)) - set(arr)
    return min(diff) + 1 if diff else None
