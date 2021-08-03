def even_numbers(arr, n):
    evenlist = []
    for x in arr:
        if x % 2 == 0:
            evenlist.append(x)
    return evenlist[-n:]
