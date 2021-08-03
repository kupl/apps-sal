def odd_one(arr):
    for index, value in enumerate(arr):
        if value % 2 != 0:
            break
    return -1 if value % 2 == 0 else index
