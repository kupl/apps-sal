def isValid(seq):
    return (7 in seq or 8 in seq) and ((5 in seq and 6 in seq) or (5 not in seq and 6 not in seq)) and (1 not in seq or 2 not in seq) and (3 not in seq or 4 not in seq)
