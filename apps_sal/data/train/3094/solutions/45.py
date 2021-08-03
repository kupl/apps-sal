def sum_array(arr):
    if not arr:
        return 0

    if len(arr) < 3:
        return 0
    return sum(sorted(arr)[1: len(arr) - 1])
