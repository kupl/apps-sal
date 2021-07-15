def find_in_array(seq, predicate):
    return next((i for i, e in enumerate(seq) if predicate(e, i)), -1)
