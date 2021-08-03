def nth_smallest(arr, pos):
    return sorted(arr, reverse=True)[pos * -1]
