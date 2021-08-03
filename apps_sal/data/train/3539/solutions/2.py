def norm_index_test(seq, ind):
    try:
        return seq[ind % len(seq)]
    except:
        pass
