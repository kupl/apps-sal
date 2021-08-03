def hot_singles(arr1, arr2):
    return sorted(set(arr1).symmetric_difference(set(arr2)), key=(arr1 + arr2).index)
