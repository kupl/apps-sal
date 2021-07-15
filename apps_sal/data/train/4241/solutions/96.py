def sequence_sum(begin_number, end_number, step):
    x =[]
    count = begin_number
    if begin_number > end_number:
        return 0
    while count <= end_number:
        x.append(count)
        count += step
    return sum(x)
