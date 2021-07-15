def sequence_sum(begin_number, end_number, step):
    sum_total = 0
    for num in range(begin_number, end_number + 1, step):
        sum_total += num
    return sum_total
