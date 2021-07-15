def even_numbers(arr,n):
    newarr = []
    for i in arr:
        if i % 2 == 0:
            newarr.append(i)
    return newarr[-n:]
