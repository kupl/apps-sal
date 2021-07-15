def first_non_consecutive(arr):
    results = set(range(arr[0], arr[-1])) - set(arr)
    return min(results)+1 if len(results) > 0 else None
