def sequence_sum(begin, end, step):
    if begin>end:
        return 0
    sum = 0
    for x in range(begin,end+step,step):
        if x>end:
            break
        sum+=x
    return sum
