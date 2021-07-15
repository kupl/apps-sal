def colour_association(arr):
    array = []
    for pair in arr:
        array.extend([{pair[0] : pair[1]}])
    return array
