def distinct(seq):
    array = []
    for x in seq:
        if x not in array:
            array.append(x)
    return array
