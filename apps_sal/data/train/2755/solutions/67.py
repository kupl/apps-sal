def multiple_of_index(arr):
    return [i for j,i in enumerate(arr) if j != 0 and i%j == 0]
