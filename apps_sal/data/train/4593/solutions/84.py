def merge_arrays(arr1, arr2):
    arr1.sort()
    arr2.sort()
    c = []
    for i in arr1:
        c.append(i)
    for i in arr2:
        c.append(i)
    from collections import OrderedDict
    u = list(OrderedDict.fromkeys(c))
    u.sort()
    return u
