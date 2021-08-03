def find_uniq(arr):
    s = set(arr)
    for e in s:
        if arr.count(e) == 1:
            return e
