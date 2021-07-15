def find_longest(arr):
    r = [len(str(x)) for x in arr]
    return arr[r.index(max(r))]
