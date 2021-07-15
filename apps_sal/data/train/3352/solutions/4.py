def find_longest(arr):
    e = [len(str(i)) for i in arr]
    return arr[e.index(max(e))]
