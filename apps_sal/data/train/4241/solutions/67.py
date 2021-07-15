def sequence_sum(begin_number, end_number, step):
    return sum([n for n in range(begin_number, end_number+1, step)]) if begin_number <= end_number else 0

