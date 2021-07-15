def merge_arrays(arr1, arr2):
    emptylist = []
    for eachnumber in arr1:
        if eachnumber in emptylist:
            continue
        else:
            emptylist.append(eachnumber)
    for eachnumber in arr2:
        if eachnumber in emptylist:
            continue
        else:
            emptylist.append(eachnumber)
    emptylist.sort()
    return emptylist
