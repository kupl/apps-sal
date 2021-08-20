def is_thue_morse(seq):
    (tm, lt, ls) = ([0], 1, len(seq))
    while lt <= ls:
        if seq[:lt] != tm:
            return False
        tm.extend([not d for d in tm])
        lt *= 2
    return tm[:ls] == seq
