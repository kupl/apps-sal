def sequence_sum(bn, end, step):
    print(bn, end, step)
    sum = 0
    if bn > end:
        return 0
    for i in range(bn, end+1, step):
        sum += i
    return sum
