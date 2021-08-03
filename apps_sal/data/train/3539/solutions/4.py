def norm_index_test(seq, ind):
    return None if len(seq) == 0 else seq[ind % len(seq)]
