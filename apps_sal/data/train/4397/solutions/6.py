def is_thue_morse(seq):
    s = [0]
    while len(s) < len(seq):
        s += [1 - v for v in s]
    return s[:len(seq)] == seq
