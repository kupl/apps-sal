def sequence_sum(begin, end, step):
    d = []
    for i in range(begin, end + 1, step):
        d.append(i)
    return sum(d)
