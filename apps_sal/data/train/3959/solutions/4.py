def max_sum(arr, ranges):
    return max(sum(arr[a:b + 1]) for a, b in ranges)
