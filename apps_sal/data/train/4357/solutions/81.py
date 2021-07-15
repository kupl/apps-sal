def nth_smallest(arr, pos):
    sorted_arr = sorted(arr)
    while pos > 1:
        sorted_arr.pop(0)
        pos -= 1
    return sorted_arr.pop(0)
