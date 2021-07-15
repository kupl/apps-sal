def sequence_sum(begin_number, end_number, step):
    if begin_number <= end_number:
        num = begin_number
        fin = begin_number
        while num <= end_number:
            num += step
            fin += num
        if fin > end_number:
            fin -= num
        return fin
    else:
        return 0
