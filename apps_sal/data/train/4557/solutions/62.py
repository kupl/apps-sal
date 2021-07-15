def row_weights(array):
    first_command = 0
    second_command = 0
    for index, value in enumerate(array, 1):
        if index % 2 == 0:
            second_command += value
        else:
            first_command += value
    return first_command, second_command
