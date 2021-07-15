def sum_mix(arr):
    tot = 0
    for i in range(len(arr)):
        if type(arr[i]) is str:
            x = int(arr[i])
            tot += x
        else:
            tot += arr[i]
    return tot

