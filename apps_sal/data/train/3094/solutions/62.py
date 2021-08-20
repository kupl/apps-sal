def sum_array(arr):
    sum = 0
    if not arr or len(arr) == 1:
        return 0
    else:
        for i in arr:
            sum = sum + i
        return sum - min(arr) - max(arr)
