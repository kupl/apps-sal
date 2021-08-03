def sequence_sum(begin_number, end_number, step):
    if (begin_number > end_number):
        return 0

    if (begin_number == end_number):
        return begin_number

    sum = begin_number
    curr = begin_number + step

    while curr <= end_number:
        sum += curr
        curr = curr + step

    return sum
