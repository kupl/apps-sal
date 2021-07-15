def first_non_consecutive(arr):
    return None if len(arr) < 2 else (arr[1] if arr[1]-arr[0] != 1 else first_non_consecutive(arr[1::]))
