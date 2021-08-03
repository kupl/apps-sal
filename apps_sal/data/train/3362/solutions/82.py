def sum_mix(arr):
    t = 0
    for i in arr:
        if isinstance(i, str):
            t += int(i)
        else:
            t += i
    return t
