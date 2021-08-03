def sequence_sum(begin_number, end_number, step):
    out = 0
    while begin_number <= end_number:
        out += begin_number
        begin_number += step
    return out
