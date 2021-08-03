def almost_increasing_sequence(sequence):

    for n, i in enumerate(sequence):
        lis = sequence.copy()
        del(lis[n])
        if len(lis) == len(set(lis)):
            if sorted(lis) == lis:
                return True

    return False
