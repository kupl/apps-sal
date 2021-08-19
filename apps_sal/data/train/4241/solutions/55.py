def sequence_sum(begin_number, end_number, step):
    if begin_number <= end_number:
        return sum((x for x in range(begin_number, end_number + 1, step)))
    else:
        return 0
