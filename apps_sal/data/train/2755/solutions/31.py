def multiple_of_index(arr):
    new = []
    i = 1
    while i < len(arr):
        if arr[i] % i == 0:
            new.append(arr[i])
        i += 1
    return new
