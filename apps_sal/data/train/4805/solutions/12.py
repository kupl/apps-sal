def check(seq, elem):
    i = 0
    while i < len(seq):
        if elem == seq[i]:
            return True
        elif elem != seq[i] and i != len(seq) - 1:
            i = i + 1
        elif elem != seq[i] and i == len(seq) - 1:
            return False
