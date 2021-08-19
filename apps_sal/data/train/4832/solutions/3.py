def all_non_consecutive(arr):
    return [{'i': i + 1, 'n': n} for (i, n) in enumerate(arr[1:]) if arr[i + 1] - arr[i] != 1]
