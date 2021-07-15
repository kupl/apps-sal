def sequence_sum(begin_number, end_number, step):
    number = 0
    while not begin_number > end_number:
        number += begin_number
        begin_number += step
    return number
