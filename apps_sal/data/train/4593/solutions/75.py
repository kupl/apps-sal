def merge_arrays(arr1, arr2):

    arr3 = sorted(arr1+arr2)

    for i in range(len(arr3)):
        for j in range(0,len(arr3) - 1 - i):
            if arr3[i] == arr3[i+1]:
                del arr3[i]
            else:
                continue
    return arr3
