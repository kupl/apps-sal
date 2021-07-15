def unflatten(flat_array):
    result = []
    i = 0
    while i < len(flat_array):
        num = flat_array[i]
        if num <= 2:
            result.append(num)
            i += 1
        else:
            result.append(flat_array[i:i+num])
            i += num
    return result
