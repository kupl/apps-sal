def move_zeros(array):
    zeros = 0
    new_arr = []
    for ele in array:
        if type(ele).__name__ != 'str' and str(ele) in '0.0':
            zeros += 1
        else:
            new_arr += [ele]
    return new_arr + [0] * zeros
