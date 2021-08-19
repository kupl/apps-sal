def all_non_consecutive(arr):
    return [{'i': i, 'n': n} for (i, n) in enumerate(arr[1:], 1) if arr[i - 1] != n - 1]
