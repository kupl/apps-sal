def sequence_sum(begin, end, step):
    return sum(_ for _ in range(begin, end + 1, step)) if end >= begin else 0
