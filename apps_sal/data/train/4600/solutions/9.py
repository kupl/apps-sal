def move_zeros(array):
    temp = []
    for e in array[::-1]:  # traverse array in reverse
        if type(e) in (int, float, complex) and e == 0:  
            # number equivalent to 0 identified. Add 0 to the end of the new array.
            temp.append(0)
        else:
            # something else, add it to the beginning of the new array.
            temp.insert(0, e)
    array = temp
    return array
