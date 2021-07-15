def nth_smallest(arr, n):
    sorted_arr = sorted(set(arr))
    if n <= len(sorted_arr):
        return sorted_arr[n - 1]
