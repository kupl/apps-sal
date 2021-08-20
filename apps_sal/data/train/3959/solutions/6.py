def max_sum(arr, ranges):
    return max((sum(arr[p[0]:p[1] + 1]) for p in ranges)) if ranges else 0
