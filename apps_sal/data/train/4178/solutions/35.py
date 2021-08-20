def min_sum(arr):
    sum_numbers = 0
    n = int(len(arr) / 2)
    for operation in range(n):
        b = max([i for i in arr])
        c = min([i for i in arr])
        v = b * c
        sum_numbers = sum_numbers + v
        arr == arr.remove(b)
        arr == arr.remove(c)
    return sum_numbers
    pass
