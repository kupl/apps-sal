def complete_series(seq):
    return list(range(max(seq) + 1)) if len(seq) == len(set(seq)) else [0]
