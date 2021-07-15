def repeats(arr):
    return sum([x for x in arr if arr.count(x) == 1])
