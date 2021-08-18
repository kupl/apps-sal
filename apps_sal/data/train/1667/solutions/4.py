def unflatten(flat_array, depth):
    left = True
    i = 0
    new_array = flat_array

    for d in range(depth):
        new_array = unflatten_list(new_array, left, i)
        left = not left
        if left:
            i = 0
        else:
            i = len(new_array) - 1
    return new_array


def unflatten_list(array, direction, i):
    new_list = []
    while (direction == True and i < len(array)) or (direction == False and i >= 0):
        elem = array[i]
        if type(elem) == list:
            if direction:
                index = 0
                new_list.append(unflatten_list(elem, direction, index))
                i += 1
            else:
                index = len(elem) - 1
                new_list.insert(0, unflatten_list(elem, direction, index))
                i -= 1
        else:
            if direction:
                residual = elem % (len(array) - i)
            else:
                residual = elem % (i + 1)
            if residual < 3:
                if direction:
                    new_list.append(elem)
                    i += 1
                else:
                    new_list.insert(0, elem)
                    i -= 1
            else:
                if direction:
                    if(i + residual <= len(array)):
                        new_list.append(array[i:i + residual])
                        i = i + residual
                    else:
                        new_list.append(array[i:])
                        i = len(array)
                else:
                    if(i - residual <= len(array)):
                        new_list.insert(0, array[i - residual + 1: i + 1])
                        i = i - residual
                    else:
                        new_list.insert(0, array[:i + 1])
                        i = -1

    return new_list
