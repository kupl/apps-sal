def distinct(seq):
    bob = []
    i = 0
    while i < len(seq):
        if seq[i] not in bob:
            bob.append(seq[i])
        i += 1

    return bob
