def all_non_consecutive(arr):
    return [{'n': e, 'i': i} for i, e in enumerate(arr[1:], 1) if e - arr[i - 1] > 1]
