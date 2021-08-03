def sum_array(arr):
    sum = 0
    if arr == None or len(arr) < 3:
        return sum
    arr.sort()
    for i in range(1, len(arr) - 1):
        sum += arr[i]
    return sum
