def sequence_sum(begin, end, step):
    arr = []
    if begin > end:
        return 0
    while begin <= end:
        arr.append(begin)
        begin = begin + step
    return sum(arr)
