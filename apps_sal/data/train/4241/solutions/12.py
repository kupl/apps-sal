def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
        return 0
    n = (end_number - begin_number) // step
    return begin_number * (n + 1) + step * n * (n + 1) // 2
