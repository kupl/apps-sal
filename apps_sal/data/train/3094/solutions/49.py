def sum_array(arr):
    if arr is None:
        return 0
    for el in arr:
        if type(el) == int and type(el) != 'NoneType' and (len(arr) > 2):
            arr.remove(max(arr))
            arr.remove(min(arr))
            print(arr)
            return sum(arr)
        else:
            return 0
    return sum(arr)
