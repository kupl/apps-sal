def sequence_sum(begin_number, end_number, step):
    return_sum = 0
    stepper = begin_number
    while stepper <= end_number:
        return_sum += stepper
        stepper += step
    return return_sum

