def even_numbers(arr,n):
    x = []
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            x.append(arr[i])
    res = len(x) - n
    return x[res:]
