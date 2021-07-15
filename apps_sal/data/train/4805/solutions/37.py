def check(seq, elem):
    truth = False
    for terms in seq:
        if terms == elem:
            truth = True
            break
    return truth
