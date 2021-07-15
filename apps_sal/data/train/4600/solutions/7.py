def move_zeros(array):
    return [x for x in array if x != 0 or x is False]+[x for x in array if x == 0 and not(x is False)]
