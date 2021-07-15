def merge_arrays(arr1, arr2):
    a = sorted(arr1+arr2)
    ant = a[0]
    for x in a[1:]:
        if x == ant:
            a.remove(x)
            ant = x
        else:
            ant = x
    return a
