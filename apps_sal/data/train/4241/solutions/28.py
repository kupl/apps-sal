def sequence_sum(begin_number, end_number, step):
    return sum([0 if begin_number > end_number else begin_number + 
                sequence_sum(begin_number + step, end_number, step)])
