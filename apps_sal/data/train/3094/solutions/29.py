def sum_array(arr):
    if arr == None:
        return 0
    if len(arr) <= 2:
        return 0
    else:
        arr.sort()
        del arr[0]
        del arr[-1]
        return sum(arr)
