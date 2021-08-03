def odd_one(arr):
    for i in arr:
        if i % 2:
            return arr.index(i)
    return -1
