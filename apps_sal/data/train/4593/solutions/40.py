def merge_arrays(arr1, arr2):
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    (i, j) = (0, 0)
    result = []
    while True:
        if i == len(arr1):
            result.extend(arr2[j:])
            break
        elif j == len(arr2):
            result.extend(arr1[i:])
            break
        elif arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    unique = []
    for num in result:
        if num not in unique:
            unique.append(num)
    return unique
