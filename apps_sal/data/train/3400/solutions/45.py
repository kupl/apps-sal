def even_numbers(arr, n):
    evens = []
    for i in arr:
        if i % 2 == 0:
            evens.append(i)
    if len(evens) == n:
        return evens
    else:
        del evens[:-n]
        return evens
