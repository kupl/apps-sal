def sequence_sum(bn, end, step):
    if bn > end:
        return 0
    else:
        return bn + sequence_sum(bn + step, end, step)
