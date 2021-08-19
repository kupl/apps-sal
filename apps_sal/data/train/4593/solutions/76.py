def merge_arrays(arr1, arr2):
    if arr1 == [] and arr2 == []:
        return []
    else:
        s = [*arr1, *arr2]
        t = list(set(s))
        t.sort()
        return t
