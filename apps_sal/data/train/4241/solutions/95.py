def sequence_sum(begin_number, end_number, step):
    if end_number < begin_number:
        return 0
    i = 0
    for z in range(begin_number, end_number + 1, step):
        i += z
    return i
