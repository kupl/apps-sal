def sum_array(arr):
    try:
        if len(arr) > 2:
            arr.sort()
            return sum(arr[1:-1])
        else:
            return 0
    except TypeError:
        return 0
