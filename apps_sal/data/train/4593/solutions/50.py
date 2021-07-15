def merge_arrays(arr1, arr2):
    # Merge arrays whithout duplicates
    arr = []
    for i in range(len(arr1)):
        if arr1[i] not in arr:
            arr.append(arr1[i])
    for i in range(len(arr2)):
        if arr2[i] not in arr:
            arr.append(arr2[i])
    # Selection sort arrays
    for i in range(len(arr)):
        m = min(arr[i:])
        index = arr.index(m)
        
        temp = arr[i]
        arr[i] = m
        arr[index] = temp
    return arr
            

