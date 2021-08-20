def move_zeros(array):
    temp = []
    for e in array[::-1]:
        if type(e) in (int, float, complex) and e == 0:
            temp.append(0)
        else:
            temp.insert(0, e)
    array = temp
    return array
