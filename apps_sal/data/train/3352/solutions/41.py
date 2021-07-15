def find_longest(arr):
    res = ''
    for i in arr:
        if len(str(res)) < len(str(i)):
            res = i
    return res
