def sequence_sum(begin, end, step):
    x = begin
    sum = 0
    while x <= end:
        sum = sum + x
        x = x + step
    return sum
