def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
        number = 0
    else:
        number = begin_number
    while begin_number + step <= end_number:
        begin_number += step
        number += begin_number
    return number
