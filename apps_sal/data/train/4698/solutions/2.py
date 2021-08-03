def is_int_array(arr):
    if arr is None or type(arr) is str or None in arr:
        return False
    else:
        for i in arr:
            if type(i) is str or i % 1 != 0:
                return False
    return True
