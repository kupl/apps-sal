def nth_smallest(arr, pos):
    if pos > len(arr):
        return sorted(arr)[-1]
    else:
        return sorted(arr)[pos - 1]
