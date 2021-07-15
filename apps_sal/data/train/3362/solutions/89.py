def sum_mix(arr):
    sum = 0
    for x in arr:
        if type(x) == str:
            x = int(x)
            sum = sum + x
        else:
            sum = sum + x

    return sum
