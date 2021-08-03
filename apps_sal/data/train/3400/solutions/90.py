def even_numbers(arr, n):
    lst = []
    for i in arr:
        if i % 2 == 0:
            lst.append(i)
    return lst[-n:]
