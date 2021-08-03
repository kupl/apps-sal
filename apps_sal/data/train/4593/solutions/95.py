def merge_arrays(arr1, arr2):
    p = list(set(arr1).union(set(arr2)))
    for i in range(0, len(p) - 1):
        for j in range(i, len(p)):
            if p[j] < p[i]:
                temp = p[i]
                p[i] = p[j]
                p[j] = temp
            else:
                pass
    return p
