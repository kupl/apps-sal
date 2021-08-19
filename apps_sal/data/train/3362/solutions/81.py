def sum_mix(arr):
    sum = 0
    for i in range(len(arr)):
        if isinstance(arr[i], str):
            sum += int(arr[i])
        else:
            sum += arr[i]
    return sum
