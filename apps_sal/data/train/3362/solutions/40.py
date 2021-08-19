def sum_mix(arr):
    sum = 0
    for i in range(len(arr)):
        if arr[i] is int:
            sum += 0
        else:
            sum += int(arr[i])
    return sum
