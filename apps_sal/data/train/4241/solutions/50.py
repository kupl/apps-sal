def sequence_sum(begin_number, end_number, step):
    out = 0
    for i in range(begin_number, end_number + 1, step):
        out += i
    return out
