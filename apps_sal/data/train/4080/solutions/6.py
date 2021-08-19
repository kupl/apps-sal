def arr_check(arr):
    for i in arr:
        try:
            i.append('')
        except:
            return False
    return True
