def multiple_of_index(arr):
    return [i for num, i in enumerate(arr[1:],1) if i % num == 0]

