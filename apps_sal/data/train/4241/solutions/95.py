def sequence_sum(begin_number, end_number, step):
    if end_number < begin_number:  # check if beginning is bigger then end
        return 0
    i = 0  # initialize loop
    for z in range(begin_number, end_number + 1, step):
        i += z
    return i
