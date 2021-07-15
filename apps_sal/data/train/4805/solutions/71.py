def check(seq, elem):
    bool = False
    for i in range(len(seq)):
        if seq[i] == elem:
            bool = True
    return bool
