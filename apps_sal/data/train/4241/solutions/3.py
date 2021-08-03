def sequence_sum(begin, end, step):
    # if begin_number > end_number:
    #     return 0
    # else:
    #     #begin_number <= end_number:
    #     return sum(begin_number, end_number)

    if begin > end:
        return 0
    else:
        return begin + (sequence_sum(begin + step, end, step))
