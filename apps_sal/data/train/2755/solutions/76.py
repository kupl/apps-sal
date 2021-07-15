def multiple_of_index(arr):
    multiple_list = []
    for i in range(1,len(arr)):
        if arr[i] % i == 0:
            multiple_list.append(arr[i])
    return multiple_list
