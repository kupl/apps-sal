def even_numbers(arr, num):
    new = []
    for i in arr:
        if i % 2 == 0:
            new.append(i)
    return new[-num:]
