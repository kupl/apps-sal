def sequence_sum(begin_number, end_number, step):
    if begin_number==end_number:
        return begin_number
    elif begin_number > end_number:
        return 0
    else:
        return sequence_sum(begin_number + step,end_number, step)+ begin_number
