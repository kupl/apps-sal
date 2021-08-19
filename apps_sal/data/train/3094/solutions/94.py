def sum_array(arr):
    if arr == None:
        return False
    elif len(arr) == 1 or len(arr) == 0:
        return 0
    sum = 0
    minimum = min(arr)
    maximum = max(arr)
    for i in arr:
        sum += i
    return sum - minimum - maximum
