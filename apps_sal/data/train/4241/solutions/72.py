def sequence_sum(begin_number, end_number, step):
    sum = 0
    if begin_number > end_number:
        return 0
    for x in range(begin_number, end_number + 1, step):
        print(x)
        sum = sum + x
    return sum
