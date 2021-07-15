def sum_array(arr):
    if arr == None or len(arr) < 2:
        return 0
    arr = sorted(arr)
    arr.pop(0)
    arr.pop(-1)
    return sum(arr)

