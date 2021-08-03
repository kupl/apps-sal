def unflatten(flat_array, depth, direction=1):
    if depth == 0:
        return flat_array
    ind = 0
    array = []
    flat_array = flat_array[::direction]
    while ind < len(flat_array):
        nleft = len(flat_array) - ind
        elem = flat_array[ind]
        if type(flat_array[ind]) is list:
            array.append(unflatten(flat_array[ind], 1, direction))
            ind += 1
        elif elem % nleft < 3:
            array.append(elem)
            ind += 1
        else:
            array.append(flat_array[ind:ind + elem % nleft][::direction])
            ind += elem % nleft
    return unflatten(array[::direction], depth - 1, -direction)
