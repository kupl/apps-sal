def is_int_array(arr):
    if arr == []:
        return True
    if arr in [None, '']:
        return False
    for i in arr:
        if type(i) in [int, float]:
            if int(i) != i:
                return False
        else:
            return False
    return True
