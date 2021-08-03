def sequence_sum(begin_number, end_number, step):
    sum = 0
    if begin_number <= end_number:
        while begin_number <= end_number:
            sum += begin_number
            begin_number += step
        if begin_number < end_number:
            sum += begin_number
        return sum
    elif step >= begin_number - end_number or begin_number > end_number:
        return 0
