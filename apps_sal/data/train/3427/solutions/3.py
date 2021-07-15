def find_uniq(arr):
    a = sorted(arr)
    return a[0] if a[0] != a[1] else a[-1]
