def sum_array(arr):
    if arr == None:
        return 0
    elif len(arr) <= 2:
        return 0

    arr.sort()
    return sum(arr[1:-1])
