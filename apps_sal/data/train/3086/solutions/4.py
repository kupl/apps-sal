def unflatten(flat_array):
    new_array = []
    i = 0
    while i < len(flat_array):
        if flat_array[i] < 3:
            new_array.append(flat_array[i])
            i+=1
        else:
            new_array.append(flat_array[i:i+flat_array[i]])
            i+=flat_array[i]
    return new_array
