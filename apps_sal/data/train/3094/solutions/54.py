def sum_array(arr):
    sum = 0
    if arr == '':
        return 0
    elif arr == None:
        return 0
    elif len(arr) < 3:
        return 0
    else:
        for i in arr:
            sum += i
        return sum - (min(arr) + max(arr))
