def sequence_sum(begin_number, end_number, step):
    if end_number >= begin_number:
        return sum(range(begin_number, end_number + 1, step))
    else:
        return 0
