def norm_index_test(seq, ind):
    if seq:
        return seq[ind%len(seq)]
    return None
