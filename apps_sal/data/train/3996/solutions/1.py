def alternate_sq_sum(arr):
    return sum((x * x for x in arr[1::2])) + sum(arr[::2])
