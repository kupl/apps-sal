def positive_sum(arr):
    sum = 0
    for n in range(0, len(arr)):
        if arr[n] > 0:
            sum += arr[n]
    return sum
