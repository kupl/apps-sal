def multiple_of_index(arr):
    arr.pop(0)
    return list((b for (a, b) in list(enumerate(arr, start=1)) if b % a == 0))
