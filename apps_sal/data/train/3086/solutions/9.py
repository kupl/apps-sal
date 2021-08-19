def unflatten(flat_array):
    new_array = []
    start = 0
    while start < len(flat_array):
        if flat_array[start] < 3:
            new_array.append(flat_array[start])
            start += 1
        else:
            new_array.append(flat_array[start:start + flat_array[start]])
            start += flat_array[start]
    return new_array
