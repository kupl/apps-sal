def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
        return 0
    n = int((end_number - begin_number) / step)
    end_number = begin_number + step * n
    return int((begin_number + end_number) * (n + 1) * 0.5)
