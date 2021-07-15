def total(arr):
    while len(arr) > 2:
        arr = [x + y for x, y in zip(arr, arr[1:])]
    return sum(arr)
