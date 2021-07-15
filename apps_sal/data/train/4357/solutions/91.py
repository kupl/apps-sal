def nth_smallest(arr, pos):
    sort = sorted(arr)
    print(sort)
    for i in range(len(sort)):
        if i == pos - 1:
            return sort[i]
