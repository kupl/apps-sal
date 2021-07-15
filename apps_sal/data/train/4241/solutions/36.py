def sequence_sum(begin_number, end_number, step):
    num_list = []
    current_num = begin_number
    if begin_number > end_number:
        return 0
    elif begin_number == end_number:
        return begin_number
    else:
        while current_num <= end_number:
            num_list.append(current_num)
            current_num += step
    return sum(num_list)
