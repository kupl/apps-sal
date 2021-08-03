def sequence_sum(start, end, step):
    if start > end:
        return 0
    return sum(x for x in range(start, end + 1, step))
