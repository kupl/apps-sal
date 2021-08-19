def multiple_of_index(arr):
    lst = []
    for i in range(len(arr)):
        if i == 0:
            if arr[i] == 0:
                lst.append(arr[i])
        elif arr[i] % i == 0:
            lst.append(arr[i])
    return lst
