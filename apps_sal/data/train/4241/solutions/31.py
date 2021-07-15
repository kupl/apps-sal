def sequence_sum(begin_number, end_number, step):
    sq = []
    for i in range(begin_number, end_number + 1, step):
        sq.append(i)
    return sum(sq)
