def merge_arrays(arr1, arr2):
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    i = 0
    j = 0
    sol = []
    if len(arr1) + len(arr2) == 0:
        return []
    for h in range(len(arr1) + len(arr2)):
        if j == len(arr2):
            sol.append(arr1[i])
            i += 1
        elif i == len(arr1):
            sol.append(arr2[j])
            j += 1
        elif arr1[i] <= arr2[j]:
            sol.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            sol.append(arr2[j])
            j += 1
    return sorted(set(sol), key=sol.index)
