def max_sum(arr, ranges):
    return max(sum(arr[start:end + 1]) for start, end in ranges)
