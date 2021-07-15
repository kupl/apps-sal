def move_zeros(array):
    return sorted(array, key=lambda x: x == 0 and x is not False)
