def hot_singles(arr1, arr2):
    vals = arr1 + arr2
    return sorted(set(arr1).symmetric_difference(arr2), key=vals.index)
