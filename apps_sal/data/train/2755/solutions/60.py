def multiple_of_index(arr):
    new_arr = []
    for i in range(len(arr)):
        if i == 0:
            continue
        elif arr[i] % i == 0:
            new_arr.append(arr[i])
    return new_arr
