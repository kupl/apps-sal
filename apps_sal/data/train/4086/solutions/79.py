def first_non_consecutive(arr):
    size = len(arr)
    for i in range(size):
        if i == size-1:
            return None
        elif arr[i+1] > arr[i]+1:
            return arr[i+1]
