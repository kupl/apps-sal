def sequence_sum(a, b, c):
    r = []
    while a <= b:
        r.append(a)
        a += c
    return sum(r)
