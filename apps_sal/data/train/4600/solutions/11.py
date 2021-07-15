def move_zeros(array):
    a_len = len(array)
    array = [v for v in array if type(v) is bool or v != 0]
    array.extend([0]*(a_len-len(array)))
    return array
