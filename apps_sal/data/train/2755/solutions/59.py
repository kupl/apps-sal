def multiple_of_index(arr):
    return [b for a, b in enumerate(arr[1:], 1) if b % a == 0]
