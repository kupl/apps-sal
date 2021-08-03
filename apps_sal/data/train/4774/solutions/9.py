def find_in_array(seq, predicate):
    for i, elem in enumerate(seq):
        if predicate(elem, i):
            return i
    return -1
