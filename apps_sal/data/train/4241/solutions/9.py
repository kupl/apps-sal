def sequence_sum(begin_number, end_number, step):
    output = 0
    for x in range(begin_number, end_number + 1, step):
        output = output + x
    return output
