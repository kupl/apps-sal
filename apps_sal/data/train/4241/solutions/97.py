def sequence_sum(begin_number, end_number, step):
    accum = 0
    for i in range(begin_number, end_number+1, step):
        accum += i
    return accum
