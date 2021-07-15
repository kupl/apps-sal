def even_numbers(arr,n):
    a = []
    for i in arr:
        if i % 2 == 0:
            a.append(i)
    return a[len(a) - n:]
