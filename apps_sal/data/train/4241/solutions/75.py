def sequence_sum(begin_number, end_number, step):
    steps = (end_number - begin_number) // step + 1
    return steps * begin_number + step * steps * (steps - 1) / 2 if steps > 0 else 0
