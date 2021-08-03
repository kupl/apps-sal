def sequence_sum(b, e, s):
    c = 0
    for i in range(b, e + 1, s):
        c += i
    return c
