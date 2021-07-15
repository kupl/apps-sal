def get_min_max(seq):
    seq.sort()
    return (seq[0],seq[0]) if len(seq) is 1 else (seq[0],seq[len(seq)-1])

