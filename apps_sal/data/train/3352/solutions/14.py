def find_longest(arr):
    return max(arr, key=lambda n: len(str(n)))
