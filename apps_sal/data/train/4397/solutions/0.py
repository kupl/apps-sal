def is_thue_morse(seq):
    init_seq = [0]
    while len(init_seq) < len(seq):
        init_seq += [1 if n == 0 else 0 for n in init_seq]
    return init_seq[:len(seq)] == seq

