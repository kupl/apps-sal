def sequence_sum(beg, end, step):
    if beg > end:
        return 0
    return beg + sequence_sum(beg+step, end, step)

