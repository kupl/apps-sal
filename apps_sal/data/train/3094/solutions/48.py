def sum_array(arr):
    if arr == None:
        return 0
    if len(arr) > 1:
        return sum(sorted(arr)[1:-1])
    else:
        return 0
