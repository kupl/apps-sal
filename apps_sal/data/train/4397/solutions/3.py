def is_thue_morse(seq):
    return seq[0] == 0 and all(seq[i // 2] ^ seq[i] == i % 2 for i in range(len(seq)))
