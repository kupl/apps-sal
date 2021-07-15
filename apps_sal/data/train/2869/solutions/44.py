def distinct(seq):
    # create new array
    array = []
    for x in seq:
        if x not in array:
            array.append(x)
    return array
