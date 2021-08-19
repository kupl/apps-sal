def merge_arrays(arr1, arr2):
    x = arr1
    y = []
    for i in range(len(arr2)):
        x.append(arr2[i])
    for j in range(len(x)):
        if x[j] in y:
            y = y
        else:
            y.append(x[j])
    return sorted(y)
