def find_children(arr1, arr2):
    L = []
    for i in arr2:
        if i in arr1:
            if i not in L:
                L.append(i)
    L.sort()
    return L
