def alternate_sq_sum(arr):
    return sum(arr[::2]) + sum(map(lambda x: x * x, arr[1::2]))
