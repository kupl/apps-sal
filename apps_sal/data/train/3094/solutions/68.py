def sum_array(arr):
    if arr == [] or arr == None:
        return 0
    elif len(arr) > 2:
        return sum(sorted(arr)[1:-1])
    else:
        return 0
