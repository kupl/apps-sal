def multiple_of_index(arr):
    new_arr = []
    i = 1
    for x in arr[1:]:
        if x % i == 0:
            new_arr.append(x)
        i += 1
    return new_arr
