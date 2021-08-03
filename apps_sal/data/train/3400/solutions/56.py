def even_numbers(arr, n):
    newl = []
    r = arr[::-1]
    for i in r:
        if i % 2 == 0:
            newl.append(i)
            if len(newl) == n:
                return newl[::-1]
            else:
                continue
