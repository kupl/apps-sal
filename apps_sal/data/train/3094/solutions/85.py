def sum_array(arr):
    print(arr)
    if not arr:
        return 0
    elif len(arr) == 1:
        return 0
    else:
        sum = 0
        x = 0
        for x in arr:
            sum += x
        return sum - max(arr) - min(arr)
