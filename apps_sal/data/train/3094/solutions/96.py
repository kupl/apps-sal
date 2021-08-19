def sum_array(arr):
    if arr == None:
        return 0
    if len(arr) == 0:
        return 0
    sum = 0
    arr.sort()
    w = arr[1:-1]
    for i in w:
        sum += i
    return sum
