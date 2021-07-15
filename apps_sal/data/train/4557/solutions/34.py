def row_weights(array):
    command_1 = array[0::2]
    command_2 = array[1::2]
    return sum(command_1), sum(command_2)
