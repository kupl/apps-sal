def all_non_consecutive(arr):
    return [{'i': i + 1, 'n': b} for i, (a, b) in enumerate(zip(arr, arr[1:])) if b - a != 1]
