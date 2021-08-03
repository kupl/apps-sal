def nth_smallest(arr, pos):
    # Alternatively, use max-heap
    return sorted(arr)[pos - 1]
