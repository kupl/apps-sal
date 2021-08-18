def sum_mix(arr):

    total = 0

    for i in range(len(arr)):
        arr[i] = int(arr[i])
        total = total + arr[i]

    return(total)
