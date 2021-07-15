def sequence_sum(begin_number, end_number, step):
    start = int(begin_number)
    end = int(end_number)
    step = int(step)
    tot = 0
    num = start
    while num <= end:
        tot = tot + num
        num = num + step
    return tot

