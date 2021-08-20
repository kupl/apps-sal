def sequence_sum(begin_number, end_number, step):
    """
    Input: three (non-negative) int values
    return the sum of a sequence of integers
    if the starting number is greater than the end number 0 is returned
    """
    res = 0
    cal_number = begin_number
    while cal_number <= end_number:
        res += cal_number
        cal_number += step
    return res
