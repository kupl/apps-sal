def max_sum(arr, ranges):
    return max( sum(arr[start:stop+1]) for start, stop in ranges )
