def sum_array(arr):

    if not arr:
        return 0
    if len(arr) == 1:
        return 0
    if len(arr) == 2:
        return 0

    return sum(sorted(arr)[1:-1])
