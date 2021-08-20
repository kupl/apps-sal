def min_sum(arr):
    sort_arr = sorted(arr)
    i = 0
    sum = 0
    while i < len(arr) / 2:
        sum += sort_arr[i] * sort_arr[-(i + 1)]
        i += 1
    return sum
