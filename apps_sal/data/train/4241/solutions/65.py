def sequence_sum(begin_number, end_number, step):
    num = range(begin_number, end_number + 1, step)
    if begin_number > end_number:
        return 0
    else:
        return sum(num)
