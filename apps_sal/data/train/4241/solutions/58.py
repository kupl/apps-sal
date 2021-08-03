def sequence_sum(begin_number, end_number, step):
    # your code here
    if begin_number == end_number:
        return end_number
    elif begin_number > end_number:
        return 0
    else:
        return begin_number + sequence_sum(begin_number + step, end_number, step)
