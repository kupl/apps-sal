def nth_smallest(arr, pos):
    for i in range(0, len(sorted(arr))):
        if i == pos - 1:
            return sorted(arr)[i]
