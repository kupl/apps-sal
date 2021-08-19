def comp(array1, array2):
    if array1 == None or array2 == None:
        return False
    tmp = sorted([s * s for s in array1])
    return tmp == sorted(array2)
