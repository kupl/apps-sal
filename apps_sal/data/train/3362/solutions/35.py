def sum_mix(arr):
    count = 0
    for i in arr:
        if type(i) == 'str': count += int(i)
        else: count += int(i)
    return count
