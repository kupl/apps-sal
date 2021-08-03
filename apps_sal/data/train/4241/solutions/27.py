def sequence_sum(begin, end, step):
    s = 0
    for i in range(begin, end + 1, step):
        s = s + i
    return s
