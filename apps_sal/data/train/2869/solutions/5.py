def distinct(seq):
    nl = []
    [nl.append(i) for i in seq if i not in nl]
    return nl
