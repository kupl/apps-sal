def sequence_sum(begin, end, step):
    if begin > end:
        return 0
    else:
        return begin + sequence_sum(begin + step, end, step)
