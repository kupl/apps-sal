def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
        end = end_number - 1
    else:
        end = end_number + 1
    return sum(range(begin_number, end, step))
