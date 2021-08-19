def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
        return 0
    else:
        num = begin_number
        s = begin_number
        for x in range(begin_number, end_number, step):
            if x > end_number - step:
                break
            else:
                num = num + step
                s = s + num
        return s
