def even_numbers(arr, n):
    x = []
    for i in arr:
        if i % 2 == 0:
            x.append(i)
    return x[-n:]
