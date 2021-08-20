def unflatten(flat_array):
    result = []
    index = 0
    while index < len(flat_array):
        value = flat_array[index]
        if value < 3:
            result.append(value)
            index += 1
        else:
            result.append(flat_array[index:index + value])
            index += value
    return result
