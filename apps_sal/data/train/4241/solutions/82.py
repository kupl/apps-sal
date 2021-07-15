def sequence_sum(begin_number, end_number, step):
    x = list(range(begin_number, end_number+1))
    return sum(x[::step])
