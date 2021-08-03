def sequence_sum(begin_number, end_number, step):

    num = 0

    if begin_number > end_number:
        return 0
    else:
        for j in range(begin_number, end_number + 1, step):
            num += j
        return num
