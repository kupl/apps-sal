def move_zeros(array):
    without_zeros = list(filter(lambda n: not n == 0 or n is False, array))
    for i in range(len(array) - len(without_zeros)):
        without_zeros.append(0)
    return without_zeros
