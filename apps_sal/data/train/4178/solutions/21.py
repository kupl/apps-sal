def min_sum(arr):
    total = 0
    for i, j in zip(sorted(arr),sorted(arr, reverse = True)):
        total += i*j
    return total/ 2
