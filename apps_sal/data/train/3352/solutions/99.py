def find_longest(arr):
    f = 0
    res = 0
    for i in arr:
        if (i // 10**f != 0 and i > res):
            res = i
            while (i // 10**f != 0):
                f += 1
    return res
