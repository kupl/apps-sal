def merge_arrays(arr1, arr2):
    l = arr1 + arr2
    l.sort()
    l1 = []
    for i in l:
        if(i not in l1):
            l1.append(i)
    return l1
