def find_uniq(arr):
    return [x for x in set(arr) if arr.count(x) == 1][0]
