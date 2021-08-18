def sum_array(arr):

    if arr == None or int(len(arr)) <= 2:
        return 0
    else:
        arr.remove(max(arr))
        arr.remove(min(arr))

        return sum(arr)
