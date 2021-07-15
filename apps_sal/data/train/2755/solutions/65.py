def multiple_of_index(arr):
    return [i for loop, i in enumerate(arr[1:]) if i % (loop + 1) == 0]
