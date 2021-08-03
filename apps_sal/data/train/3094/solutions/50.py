def sum_array(arr={}):
    if arr == None or arr == []:
        return 0
    if len(arr) > 1:
        res = sum(arr) - min(arr)
    else:
        res = sum(arr)
    return res - max(arr)
