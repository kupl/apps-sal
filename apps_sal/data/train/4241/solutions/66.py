def sequence_sum(begin_number, end_number, step):
    result = 0
    num = begin_number
    while num <= end_number:
        result += num
        num += step

    return result
