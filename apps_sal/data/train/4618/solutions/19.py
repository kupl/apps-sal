def positive_sum(arr):
    res = 0
    for i in arr:
        if not arr:
            return 0
        elif i < 0:
            continue
        else:
            res += i
    return res
