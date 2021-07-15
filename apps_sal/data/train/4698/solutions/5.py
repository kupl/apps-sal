def is_int_array(arr):
    try:
        return list(map(int, arr)) == arr
    except:
        return False
