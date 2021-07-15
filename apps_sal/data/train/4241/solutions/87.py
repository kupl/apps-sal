def sequence_sum(begin_number, end_number, step):
    print(begin_number, end_number, step)
    return sum([i for i in range(begin_number, end_number+1, step)]) if end_number>=begin_number else 0
