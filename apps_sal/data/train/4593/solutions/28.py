def merge_arrays(arr1, arr2):
    arr3 = []
    arr1 = list(set(arr1))
    arr2 = list(set(arr2))
    arr1.sort()
    arr2.sort()
    while len(arr1) > 0 and len(arr2) > 0:
        if arr1[0] < arr2[0]:
            arr3.append(arr1[0])
            del arr1[0]
        elif arr1[0] > arr2[0]:
            arr3.append(arr2[0])
            del arr2[0]
        else:
            arr3.append(arr1[0])
            del arr1[0]
            del arr2[0]
    return arr3 + arr2 if len(arr1) == 0 else arr3 + arr1
