def sum_array(arr):
    if arr == None:
        return 0
    elif len(arr) == 1:
        return 0
    else:
        sorted_arr = sorted(arr)
        return sum(sorted_arr[1:-1])

