def sum_mix(arr):
    res = 0
    for num in arr:
        if isinstance(num, str):
            res += int(num)
        else:
            res += num
    return res
