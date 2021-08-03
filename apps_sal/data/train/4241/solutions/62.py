def sequence_sum(begin_number, end_number, step):
    sum = 0
    if (begin_number == end_number):
        sum += end_number
    for i in range(begin_number, end_number, step):
        sum += i
        if (i + step == end_number):
            sum += end_number
    return sum
