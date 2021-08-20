def multiple_of_index(arr):
    my_list = []
    array = arr[1:]
    for (i, x) in enumerate(array, 1):
        if x % i == 0:
            my_list.append(x)
    return my_list
