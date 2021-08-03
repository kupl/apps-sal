def multiple_of_index(arr):
    l = []
    for i in range(len(arr)):
        if i == 0:
            continue
        elif arr[i] % i == 0:
            l.append(arr[i])
    return l
