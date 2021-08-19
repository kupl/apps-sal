def merge_arrays(arr1, arr2):
    arr3 = arr1 + arr2
    arr4 = sorted(arr3)
    uniqueList = []
    for i in arr4:
        if i not in uniqueList:
            uniqueList.append(i)
    return uniqueList
