def nth_smallest(arr, pos):
    new_list = sorted(arr, reverse=True)
    return new_list[-pos]
