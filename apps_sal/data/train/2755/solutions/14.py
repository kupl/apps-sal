def multiple_of_index(arr):
    return [v for i,v in enumerate(arr[1:]) if v%(i+1) == 0]
