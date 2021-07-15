def find_longest(arr):
    l = [len(str(a)) for a in arr]
    return arr[l.index(max(l))]
