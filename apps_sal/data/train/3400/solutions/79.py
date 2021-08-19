def even_numbers(arr, n):
    pass
    e = []
    l = len(e)
    for i in range(0, len(arr)):
        if arr[i] % 2 == 0:
            e.append(arr[i])
    return e[l - n:]
