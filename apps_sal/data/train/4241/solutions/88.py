def sequence_sum(begin_number, end_number, step):
    out = 0
    if begin_number > end_number:
        return 0
    else:
        for i in range(begin_number, end_number + 1, step):
            out += i
        return out
