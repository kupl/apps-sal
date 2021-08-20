def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
        return 0
    if begin_number == end_number:
        return end_number
    else:
        return begin_number + sequence_sum(begin_number + step, end_number, step)
