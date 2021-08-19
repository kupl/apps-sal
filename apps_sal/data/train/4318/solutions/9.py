def hot_singles(arr1, arr2):
    return sorted(set(arr1) ^ set(arr2), key=lambda x: (arr1 + arr2).index(x))
