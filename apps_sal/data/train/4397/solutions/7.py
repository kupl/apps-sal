def is_thue_morse(seq):
    return seq == [1 if bin(n).count('1')%2 else 0 for n in range(len(seq))]
