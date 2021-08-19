def multiple_of_index(arr):
    return [y for (x, y) in enumerate(arr[1:], start=1) if y % x == 0]
