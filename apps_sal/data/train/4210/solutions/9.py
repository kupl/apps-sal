def process_data(data):
    array = []
    for n in data:
        array_element = n[0] - n[1]
        array.append(array_element)
    c = 1
    for d in array:
        c *= d
    return c
