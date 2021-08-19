def check(seq, elem):
    i = 0
    for i in range(len(seq)):
        try:
            itshere = seq.index(elem)
            return True
        except ValueError:
            return False
