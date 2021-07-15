def sum_array(arr):
    if arr == None or arr == [] or len(arr) == 1:
        return 0
    else:
        arr.sort()
        arr = arr[1:-1]
        return sum(arr)
