def sequence_sum(b, e, s):
    sum = 0
    while b <= e:
        sum += b
        b += s
    return sum
