def sequence_sum(start, end, step):
    total = 0
    if end < start:
        return 0
    for x in range(start, end + 1, step):
        total += x
    return total
