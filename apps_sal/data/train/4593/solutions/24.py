def merge_arrays(arr1, arr2):
    arr1 = arr1 + arr2
    arr1 = sorted(arr1)
    a = arr1[0]
    arr = [arr1[0]]
    for x in range(1, len(arr1)):
        if arr1[x] != a:
            a = arr1[x]
            arr.append(arr1[x])
    return arr
