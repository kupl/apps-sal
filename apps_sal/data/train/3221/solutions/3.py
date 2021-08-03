def find_it(seq):
    return [x for x in seq if seq.count(x) % 2][0]
