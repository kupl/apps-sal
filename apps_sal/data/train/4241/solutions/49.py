def sequence_sum(begin_number, end_number, step):
    total = 0
    if begin_number > end_number:
        return 0
    else:
        for number in range(begin_number, end_number + 1, step):
            total += number
    return total
